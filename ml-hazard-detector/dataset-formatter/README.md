# Dataset Formatter

This project contains nessesary python scripts to extract information from the annotated synthetic dataset produced by the synthetic-dataset-generator and resphape it in an acceptable format for training.

### Disclaimer

This project creates a copy of the selected dataset produced by the synthetic-dataset-generator. Relaunching the project without output of previous runs may result in memory issues.

## Initializing

To create the dataset run:

```
python .\main.py
```

Running this project will create a directory named `dataset_v*_annotated` that contains all samples and annotations needed.
