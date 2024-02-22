# Classification

This readme file describes the classification part of the analysis.

## Environment

The classification models were trained and tested using TensorFlow (version 2.8.1) on CUDA (version 12.0). Further details are provided in [environment.yml](environment.yml) file.

## Model

The training and testing scripts are available here: https://github.com/UM2ii/SurgicalAggregation. The model checkpoint is provided [here](./checkpoint/best_metric_model_nih_224.hdf5). 

### Labels

The model outputs predictions for 14 disease labels:

> Atelectasis, Cardiomegaly, Consolidation, Edema, Emphysema, Fibrosis, Hernia, Infiltration, Mass, Nodule, Pleural Effusion, Pleural Thickening, Pneumonia, Pneumothorax 

For the analysis in this work, **only the following 7 disease labels are used**:

> Atelectasis, Cardiomegaly, Consolidation, Edema, Pleural Effusion, Pneumonia, Pneumothorax

Note that the indices of predictions follows the order of the 14 labels above (e.g., Atelectasis => 0, Cardiomegaly => 1, ..., Pneumothorax => 13). The indices of the 7 disease labels are: 

```python
[0, 1, 2, 3, 10, 12, 13]
```

## Datasets

### NIH ChestX-ray14 

The training, validation, and testing splits for the NIH dataset are provided [here](./datasets/NIH/). The given `patient_id` corresponds to `Patient ID` provided in the dataset's metadata.

### CheXpert

The training, validation, and testing splits for the NIH dataset are provided [here](./datasets/CheXpert/). The given `patient_id` corresponds to the 5 digit patient id provided in the dataset's structure. For example, a `patient_id` of 1 corresponds to the folder `patient00001/` in the dataset.

### MIMIC-CXR-JPG

The training, validation, and testing splits for the NIH dataset are provided [here](./datasets/MIMIC/). The given `patient_id` corresponds to `subject_id` provided in the dataset's metadata.