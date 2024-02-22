import os
import numpy as np
import re

VALID_FORMATS_2D = ('.jpeg', '.jpg', '.png', '.dcm', '.nrrd', '.nii', '.nii.gz')
VALID_FORMATS_3D = ('.dcm', '.nrrd', '.nii', '.nii.gz')

UINT16_MAX = 65535

# Utilities

def strip_extension(path):
  """
  Strips file extension from path.

  Arguments:
    path: A `str` path.
      - Path should point to a supported format to correctly strip file extension.
      - Unsupported formats may not work with formats such as '.tar.gz', etc.

  Returns:
    A `str` path without file extension.   
  """
  if path.lower().endswith('.nii.gz'):
    return path[:-7]
  else:
    return os.path.splitext(path)[0]

def rescale_intensities(
  img, 
  old_range = None, 
  new_range = (0,255)
):
  """
  Rescales pixel values/intensities from old range to a new range. This function is used to prevent clipping when writing and reading PGM files outside of the supported 16-bit unsigned int.

  Arguments:
    img: A `np.ndarray` object
    old_range: An ordered pair (2-tuple) of min and max pixel values from previous distritbution
    new_range: An ordered pair (2-tuple) of min and max pixel values from new distritbution

  Returns:
    An image as `np.ndarray` object with pixel values rescaled from old to new distribution
  """
  if old_range == None:
    old_min, old_max = img.min(), img.max()
  else:
    old_min, old_max = old_range
  # Don't rescale if only single value exists (for eg, peripheral dark slices)
  if old_min == old_max:
    return img
  new_min, new_max = new_range
  np.seterr(invalid='ignore')
  return ((img - old_min)/(old_max - old_min))*(new_max - new_min) + new_min

def calculate_num_decomps(shape, x_min = 64):
  """
  Calculates number of decompositions (i.e. scans/tile-parts) for optimized image-level progressive encoding.

  Arguments:
    shape: Tuple corresponding to shape of 2D data or slice from 3D data.
    x_min: Forces the native resolution of the first decomposition to exceed `x_min` and normalizes native resolutions of intermediate scans for datasets with mismatched resolutions.
    
  Returns:
    The number of decompositions as `int`.
  """
  if len(shape) != 2:
    raise ValueError('Invalid shape! `shape` must be a 2D image/slice, compatible with shape: (X,Y)')
  return int(np.log2(np.min(shape)/x_min))

def get_scan_markers(path):
  """
  Gets the byte position of the end of each tile-part from HTJ2K bytestream. This byte position will be used to slice the full bytestream for intelligent streaming.

  Arguments:
    path: A `str` path to a HTJ2K file.

  Returns:
    A `list` of final byte position of each tile-part as `int`.
  """
  SOT = b'\xff\x90'
  EOI = b'\xff\xd9'
  with open(path, 'rb') as f:
    return [i.start() for i in re.finditer(b'|'.join((SOT, EOI)), f.read())][1:]

