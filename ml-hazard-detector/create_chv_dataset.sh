#!/bin/bash

read -p "Enter full path of the CHV dataset: " BASE_PATH
read -p "Enter full path of the destination to save the dataset: " DESTINATION_PATH


python utils/chv-dataset-split.py $BASE_PATH $DESTINATION_PATH

python utils/replace_labels.py $DESTINATION_PATH/labels/train  "{'5':'2', '4':'2', '3':'2'}"

python utils/replace_labels.py $DESTINATION_PATH/labels/valid "{'5':'2', '4':'2', '3':'2'}"

python utils/replace_labels.py $DESTINATION_PATH/labels/test "{'5':'2', '4':'2', '3':'2'}"
 
echo "All scripts executed successfully"
