# AMP_prediction
----
This model is designed to predict new AMP from bacterial sORF.   
The input peptide sequence for the model must be between 5 and 40 amino acids in length.   
The scripts used for all predictions are available in the [prediction_script](https://github.com/FAFFASS/AMP_prediction/tree/main/prediction_script).   
The dataset used for training the model is stored in the [data](https://github.com/FAFFASS/AMP_prediction/tree/main/data), and the trained models are stored in the [models](https://github.com/FAFFASS/AMP_prediction/tree/main/models).

## About requirement
----
The following version information pertains to the versions used by the model runtime; other versions have not been tested.   
python3=3.9   
tensorflow=2.11   
numpy=1.25.2   
pandas=1.5.3   
scikit-learn=1.2.2   
matplotlib=3.7.1   
