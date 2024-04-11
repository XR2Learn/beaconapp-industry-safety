# Takes as input a dataset created by a fixed length Perception scenario and
# returns a new directory containing the picture files with their corresponding text with the annotated dataset

import os
import json
import shutil
import tkinter as tk
from tkinter import filedialog
import utils
import testing

root = tk.Tk()
root.withdraw()


def Create(
    dataset_path, annotated_dataset_path, debug_mode=False, write=True, sort=False
):

    index = -1

    if debug_mode:
        print("Checking if annotated dataset already exists")

    # remove annotated dataset if there is already one and create a new
    if write:
        if os.path.exists(annotated_dataset_path):
            shutil.rmtree(annotated_dataset_path)
            if debug_mode:
                print("Deleting annotated dataset")

        os.makedirs(annotated_dataset_path)
        if debug_mode:
            print("Creating new annotated dataset")

    # scan each sequence folder of dataset
    for folder in os.scandir(dataset_path):
        # skip files that are not folders
        if not folder.is_dir():
            continue

        if debug_mode:
            print(f"Entering {folder.name}")

        list_of_files = os.listdir(folder.path)

        # open json folder and copy its data
        if debug_mode:
            print(f"Reading {list_of_files[-1]}")
        json_file = open(os.path.join(folder.path, list_of_files[-1]))
        json_data = json.load(json_file)

        if not "values" in json_data["captures"][0]["annotations"][0]:
            continue

        index += 1

        # copy the last picture of the sequence in the working dir
        if write:
            shutil.copy(
                os.path.join(folder.path, list_of_files[-2]),
                os.path.join(annotated_dataset_path, f"element_{index}_picture.png"),
            )
            if debug_mode:
                print(
                    f"Copying last frame of sequence: {list_of_files[-2]} to dataset as element_{index}_picture.png"
                )

        if write:
            annotated_text = open(
                os.path.join(
                    annotated_dataset_path, f"element_{index}_annotations_.txt"
                ),
                mode="a",
            )
            if debug_mode:
                print(
                    f"Creating new text file for annotations: element_{index}_annotations_.txt"
                )

        image_dimension = json_data["captures"][0]["dimension"]
        if debug_mode:
            print(f"Dimensions of image: {image_dimension}")

        # get and normalize data of bounding box accorind to image dimensions
        if debug_mode:
            print(
                f"Bounding box in image:",
                len(json_data["captures"][0]["annotations"][0]["values"]),
                "\n",
            )

        if "values" in json_data["captures"][0]["annotations"][0]:
            for i, value in enumerate(
                json_data["captures"][0]["annotations"][0]["values"]
            ):
                [label, up_left, dimensions] = [
                    value["labelId"],
                    value["origin"],
                    value["dimension"],
                ]

                center = [
                    (up_left[0] + dimensions[0] / 2) / image_dimension[0],
                    (up_left[1] + dimensions[1] / 2) / image_dimension[1],
                ]

                dimensions = [
                    dimensions[0] / image_dimension[0],
                    dimensions[1] / image_dimension[1],
                ]

                # write line for each bounding box data
                if write:
                    annotated_text.write(
                        f"{label} {center[0]} {center[1]} {dimensions[0]} {dimensions[1]}\n"
                    )

            json_file.close()

            if write:
                annotated_text.close()

            if sort or write:
                with open(
                    os.path.join(
                        annotated_dataset_path, f"element_{index}_annotations_.txt"
                    ),
                    mode="r",
                ) as annotated_text:
                    annotations_lines = annotated_text.readlines()

                sorted_annotated_lines = sorted(
                    annotations_lines, key=lambda line: int(line.split()[0])
                )

                with open(
                    os.path.join(
                        annotated_dataset_path, f"element_{index}_annotations_.txt"
                    ),
                    mode="w",
                ) as annotated_text:
                    annotated_text.writelines(sorted_annotated_lines)


def GetAnnotatedDirectory(write=False, debug=False):
    max = 0
    for dir in os.listdir():
        if os.path.isdir(dir):
            if dir.startswith("dataset_v") and dir[6].isdigit():
                if int(dir[6]) > max:
                    max = int(dir[6])

    if write:
        new_name = "dataset_v" + str(max + 1) + "_annotated"
    else:
        new_name = "dataset_v" + str(max) + "_annotated"

    if debug:
        print("new dataset to be generated", new_name)

    return new_name


write_mode = True
debug_mode = True
sort_mode = True


selected_dataset = utils.select_dir()
generated_dataset_name = GetAnnotatedDirectory(write=write_mode, debug=debug_mode)
Create(
    selected_dataset,
    generated_dataset_name,
    write=write_mode,
    debug_mode=False,
    sort=sort_mode,
)
testing.render_random(generated_dataset_name)
