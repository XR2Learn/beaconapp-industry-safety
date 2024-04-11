"""
This script renames files within a specified directory, targeting specific substrings in filenames. It removes "_annotations_" from .txt files and "_picture" from .png files.

Usage example:
--------------

Run the script by specifying the directory containing the files you want to rename. For example:

    python rename_files.py /path/to/directory

This command will rename files in '/path/to/directory', such as changing 'file_annotations_.txt' to 'file.txt' and 'image_picture.png' to 'image.png'.
"""

import os
import sys


def rename(directory_path):
    for filename in os.listdir(directory_path):
        if filename.endswith('.txt') and "_annotations_" in filename:
            new_filename = filename.replace("_annotations_", "")
            os.rename(os.path.join(directory_path, filename), os.path.join(directory_path, new_filename))
        if filename.endswith('.png') and "_picture" in filename:
            new_filename = filename.replace("_picture", "")
            os.rename(os.path.join(directory_path, filename), os.path.join(directory_path, new_filename))

if __name__ == '__main__':
    if len(sys.argv) > 1:
        folder = sys.argv[1]
    else:
        print("Usage: python rename_files.py <folder>")
        sys.exit()

    rename(folder)
    rename(folder)







