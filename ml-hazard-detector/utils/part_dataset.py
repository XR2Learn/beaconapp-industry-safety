"""
This script splits a dataset of images and their corresponding labels into training, validation, and test sets.

It moves these files into separate subdirectories within the specified dataset folder.

Usage example:
--------------

To use the script, provide the path to the dataset folder as an argument. The folder should contain 'images' and 'labels' subfolders with corresponding files. For example:

    python split_dataset.py /path/to/dataset

After running, the dataset will be divided into training, validation, and test sets, and the files will be moved to 'images/train', 'images/val', 'images/test', 'labels/train', 'labels/val', and 'labels/test' subdirectories.
"""

import os
from sklearn.model_selection import train_test_split
import shutil
import sys

def move_files_to_folder(list_of_files, destination_folder):

    isexist = os.path.exists(destination_folder)

    if not isexist:
        os.makedirs(destination_folder)
        for f in list_of_files:
           shutil.move(f, destination_folder)

    else:
        for f in list_of_files:
           shutil.move(f, destination_folder)

if __name__ == '__main__':
    if len(sys.argv) > 1:
        folder = sys.argv[1]
    else:
        print("Usage: python split_dataset.py <folder>")
        sys.exit()

    path = '{}/labels'.format(folder)
    path2 = '{}/images'.format(folder)


    images = [os.path.join(path2, x) for x in os.listdir(path2)]
    labels = [os.path.join(path, x) for x in os.listdir(path)]

    images.sort()
    labels.sort()

    print(len(images))
    print(len(labels))

    train_images, val_images, train_annotations, val_annotations = train_test_split(images, labels, test_size = 0.2, random_state = 1)
    val_images, test_images, val_annotations, test_annotations = train_test_split(val_images, val_annotations, test_size = 0.5, random_state = 1)

    move_files_to_folder(train_images, '{}/images/train'.format(folder))
    move_files_to_folder(val_images, '{}/images/val/'.format(folder))
    move_files_to_folder(test_images, '{}/images/test/'.format(folder))
    move_files_to_folder(train_annotations, '{}/labels/train/'.format(folder))
    move_files_to_folder(val_annotations, '{}/labels/val/'.format(folder))
    move_files_to_folder(test_annotations, '{}/labels/test/'.format(folder))
