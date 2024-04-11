#!/bin/bash

read -p "Enter full path of the Synthetic dataset: " SYN_PATH

read -p "Enter full path of the CHV dataset: " CHV_PATH

echo "Creation of the dataset started..."

SCRIPT_DIR=$(dirname "$0")

BASE_DIR="$SCRIPT_DIR/combined_dataset"

if [ -d "$BASE_DIR" ]; then
    rm -rf "$BASE_DIR"
fi

NUM_OF_REAL_IMAGES=50
NUM_OF_VALIDATION_IMAGES=25
NUM_OF_SYNTHETIC_IMAGES=600

# Create the combined dataset structure
mkdir -p "$BASE_DIR/images/train"
mkdir -p "$BASE_DIR/images/val"
mkdir -p "$BASE_DIR/images/test"
mkdir -p "$BASE_DIR/labels/train"
mkdir -p "$BASE_DIR/labels/val"
mkdir -p "$BASE_DIR/labels/test"

# Move the test dataset
cp -r "$CHV_PATH/images/test/"* "$BASE_DIR/images/test"
cp -r "$CHV_PATH/labels/test/"* "$BASE_DIR/labels/test"

# Move 50 images from the RGB dataset to the train folder
IMAGE_FILES=$(find "$CHV_PATH/images/train" -type f -name '*.jpg' | shuf -n $NUM_OF_REAL_IMAGES)
for img in $IMAGE_FILES; do

    cp "$img" "$BASE_DIR/images/train"

    base=$(basename "$img" .jpg)
    label="$CHV_PATH/labels/train/${base}.txt"

    if [ -f "$label" ]; then
        cp "$label" "$BASE_DIR/labels/train"
    else
        echo "Label file for $img not found."
    fi
done

# Move 25 images from the RGB dataset to the validation folder
IMAGE_FILES=$(find "$CHV_PATH/images/valid" -type f -name '*.jpg' | shuf -n $NUM_OF_VALIDATION_IMAGES)
for img in $IMAGE_FILES; do

    cp "$img" "$BASE_DIR/images/val"

    base=$(basename "$img" .jpg)
    label="$CHV_PATH/labels/valid/${base}.txt"

    if [ -f "$label" ]; then
        cp "$label" "$BASE_DIR/labels/val"
    else
        echo "Label file for $img not found."
    fi
done

# Move 600 images from the RGB dataset to the train folder
IMAGE_FILES=$(find "$SYN_PATH/images/train" -type f -name '*.png' | shuf -n $NUM_OF_SYNTHETIC_IMAGES)
for img in $IMAGE_FILES; do

    cp "$img" "$BASE_DIR/images/train"

    base=$(basename "$img" .png)
    label="$SYN_PATH/labels/train/${base}.txt"

    if [ -f "$label" ]; then
        cp "$label" "$BASE_DIR/labels/train"
    else
        echo "Label file for $img not found."
    fi
done

echo "Dataset creation completed"
