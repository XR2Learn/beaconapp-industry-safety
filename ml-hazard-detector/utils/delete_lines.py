"""
This script processes all .txt files in a specified directory and removing classes with the given label.

Usage example:
--------------

To run the script, provide the path to the directory containing .txt files and the numbers indicating the start of lines to be deleted. For example:

    python script_name.py /path/to/directory 1 3 5

This command will process all .txt files in '/path/to/directory', removing lines that start with '1', '3', or '5'.
"""

import os
import argparse

def process_file(filepath, lines_to_delete):
    with open(filepath, 'r') as file:
        lines = file.readlines()
    
    with open(filepath, 'w') as file:
        for line in lines:
            if not any(line.startswith(str(num)) for num in lines_to_delete):
                file.write(line)

def main(directory, lines_to_delete):
    for filename in os.listdir(directory):
        if filename.endswith('.txt'):
            filepath = os.path.join(directory, filename)
            process_file(filepath, lines_to_delete)
    print("Processed all .txt files in the directory.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Process .txt files in a directory and remove specified lines.')
    parser.add_argument('folder_path', type=str, help='Path to the folder containing .txt files')
    parser.add_argument('lines_to_delete', nargs='+', type=int, help='Lines to delete (specified by starting number)')

    args = parser.parse_args()
    main(args.folder_path, args.lines_to_delete)
