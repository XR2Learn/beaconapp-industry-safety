"""
This script is designed to organize a dataset by splitting image files and label files into separate directories.

It takes a single directory containing both images (in .png format) and label files (in .txt format) and separates them into two distinct subdirectories: one for images and one for labels.

Usage example:
--------------

python split_images_labels.py /path/to/dataset_folder

"""

import os
import shutil
import sys

def split_images_labels(path):
    images_path = os.path.join(path, 'images')
    labels_path = os.path.join(path, 'labels')

    if not os.path.exists(images_path):
        os.mkdir(images_path)
    if not os.path.exists(labels_path):
        os.mkdir(labels_path)

    for file in os.listdir(path):
        if file.endswith('.txt'):
            shutil.move(os.path.join(path, file), os.path.join(labels_path, file))
        elif file.endswith('.png'):
            shutil.move(os.path.join(path, file), os.path.join(images_path, file))


if __name__ == '__main__':
    if len(sys.argv) > 1:
        split_images_labels(sys.argv[1])
    else:
        print("Usage: python split_images_labels.py <path>")
