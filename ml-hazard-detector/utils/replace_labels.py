"""
This script is designed to update label files in a given directory based on a mapping provided by the user.

Usage example:
--------------

python replace_labels.py /path/to/annotations "{'1': '3', '2': '4'}"
"""

import os
import sys
import ast  

def replace_labels(input_directory, num_map):
    for filename in os.listdir(input_directory):
        if filename.endswith(".txt"):
            input_file_path = os.path.join(input_directory, filename)
            with open(input_file_path, "r+") as input_file:
                content = input_file.readlines()
                for i, line in enumerate(content):
                    words = line.split()
                    old_num = words[0]
                    new_num = num_map.get(old_num, old_num)
                    words[0] = new_num
                    new_line = " ".join(words) + "\n"
                    content[i] = new_line
                input_file.seek(0)
                input_file.writelines(content)
                input_file.truncate()

if __name__ == '__main__':
    if len(sys.argv) > 2:
        folder = sys.argv[1]
        num_map_str = sys.argv[2]  
        num_map = ast.literal_eval(num_map_str)  
    else:
        print("Usage: python replace_labels.py <folder> '<num_map>'")
        sys.exit()

    replace_labels(folder, num_map)