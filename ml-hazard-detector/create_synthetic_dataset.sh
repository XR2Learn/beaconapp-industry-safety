#!/bin/bash

# Get path of dataset from user input
read -p "Enter full path of the synthetic dataset: " path_of_dataset

python utils/replace_labels.py "$path_of_dataset" "{'5':'0', '4':'1', '3':'2'}"

python utils/rename_images_labels.py "$path_of_dataset"

python utils/split-images-labels.py "$path_of_dataset"

python utils/part_dataset.py "$path_of_dataset"


echo "All scripts executed successfully"
