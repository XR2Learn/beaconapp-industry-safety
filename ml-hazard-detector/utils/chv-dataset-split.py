"""
This script moves image and label files from source directories to destination directories based on dataset splits defined in text files. It's useful for organizing datasets into training, testing, and validation sets.

Usage example:
--------------

To use the script, provide the base path of the dataset, and the destination path for moved files. For example:

    python script_name.py /path/to/dataset /path/to/destination

This command will read dataset split information from text files (train.txt, test.txt, valid.txt) in the 'data split' folder within the base path.
It then moves the corresponding images and labels to the specified destination, organizing them into 'train', 'test', and 'valid' subfolders.
"""

import os
import shutil
import argparse

def move_files(txt_file_path, source_image_folder, source_label_folder, destination_image_folder, destination_label_folder):

    if not os.path.exists(destination_image_folder):
        os.makedirs(destination_image_folder)
    if not os.path.exists(destination_label_folder):
        os.makedirs(destination_label_folder)

    with open(txt_file_path, 'r') as file:
        lines = file.readlines()
        for line in lines:
            line = line.strip() 
            image_filename = os.path.basename(line)
            label_filename = os.path.splitext(image_filename)[0] + '.txt'

            source_image_path = os.path.join(source_image_folder, image_filename)
            source_label_path = os.path.join(source_label_folder, label_filename)

            # Copy image file
            if os.path.exists(source_image_path):
                destination_image_path = os.path.join(destination_image_folder, image_filename)
                shutil.copy2(source_image_path, destination_image_path)
            else:
                print(f"Image file {source_image_path} does not exist.")

            # Copy label file
            if os.path.exists(source_label_path):
                destination_label_path = os.path.join(destination_label_folder, label_filename)
                shutil.copy2(source_label_path, destination_label_path)
            else:
                print(f"Label file {source_label_path} does not exist.")

parser = argparse.ArgumentParser(description='Move dataset files.')
parser.add_argument('base_path', type=str, help='Base path of the dataset')
parser.add_argument('destination_path', type=str, help='Destination path for moved files')

args = parser.parse_args()

base_path = args.base_path
destination_base = args.destination_path


data_split_path = os.path.join(base_path, 'CHV_dataset/data split')
source_image_folder = os.path.join(base_path, 'CHV_dataset/images')
source_label_folder = os.path.join(base_path, 'CHV_dataset/annotations')

splits = ['train', 'test', 'valid']

for split in splits:
    txt_file_path = os.path.join(data_split_path, f'{split}.txt')
    destination_image_folder = os.path.join(destination_base, 'images', split)
    destination_label_folder = os.path.join(destination_base, 'labels', split)
    move_files(txt_file_path, source_image_folder, source_label_folder, destination_image_folder, destination_label_folder)

print ("Process is done.")