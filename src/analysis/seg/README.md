# Segmentation

This readme file describes the segmentation part of the analysis.

## Environment

The segmentation models were trained and tested using Pytorch (version 1.13.1) on CUDA (version 11.8). Further details are provided in [environment.yml](environment.yml) file.

## Models

The training and testing scripts are available here: https://github.com/UM2ii/SegViz. The model checkpoints for both models are available [here](./checkpoint/).

## Datasets

### MSD Liver

The training and testing splits for the NIH dataset are provided [here](./datasets/MSD_Liver/). The given `image` corresponds to file names in the `imagesTr/` folder provided in the MSD Task03_Liver dataset.

### MSD Spleen

The training and testing splits for the NIH dataset are provided [here](./datasets/MSD_Spleen/). The given `image` corresponds to file names in the `imagesTr/` folder provided in the MSD Task09_Spleen dataset.

### BTCV

The testing splits for the NIH dataset are provided [here](./datasets/MSD_BTCV/). The given `image` corresponds to file names in the `Training/img/` folder provided in the Abdomen BTCV dataset.