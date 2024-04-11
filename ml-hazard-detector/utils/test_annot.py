"""
This script is designed for testing and visualizing object detection annotations.

It reads images and their corresponding label files, then draws bounding boxes around objects of a specified class. 

Usage example:
--------------

To run the script, execute it from the command line providing the base path of your dataset, the dataset type ('synthetic' or 'CHV'), and the class you want to check ('0', '1', '2', etc.). For example:

    python test_annot.py /path/to/dataset_folder synthetic 1

"""
# Script implementation follows


import cv2
import matplotlib.pyplot as plt
import os
import argparse


def draw_annotations(img_path, label_path, classs):
    img = cv2.imread(img_path)
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    dh, dw, _ = img.shape

    with open(label_path, 'r') as fl:
        data = fl.readlines()

        for dt in data:

            if not dt.startswith(classs):
                continue
            
            _, x, y, w, h = map(float, dt.split(' '))

            l = int((x - w / 2) * dw)
            r = int((x + w / 2) * dw)
            t = int((y - h / 2) * dh)
            b = int((y + h / 2) * dh)

            if l < 0:
                l = 0
            if r > dw - 1:
                r = dw - 1
            if t < 0:
                t = 0
            if b > dh - 1:
                b = dh - 1

            cv2.rectangle(img_rgb, (l, t), (r, b), (255, 0, 0), 2) 

    plt.imshow(img_rgb)
    plt.show()

def main(image_folder, label_folder, images_format, classs):
    for label_file in os.listdir(label_folder):
        if label_file.endswith('.txt'):
            img_file = label_file.replace('.txt', images_format) 

            if img_file in os.listdir(image_folder):
                img_path = os.path.join(image_folder, img_file)
                label_path = os.path.join(label_folder, label_file,)

                draw_annotations(img_path, label_path, classs)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Test the annotations')
    parser.add_argument('base_path', type=str, help='Base path of the dataset')
    parser.add_argument('dataset', type=str, help='dataset to check "synthetic" or "CHV"')
    parser.add_argument('classs', type=str, help='class to check "0", or "1" or "2"')

    args = parser.parse_args()
    
    base_path = args.base_path
    dataset = args.dataset
    classs = args.classs

    images_folder = os.path.join(base_path, 'images/train')
    labels_folder = os.path.join(base_path, 'labels/train')

    if dataset == 'synthetic':
        images_format = '.png'
    else:
        images_format = '.jpg'

    main(images_folder, labels_folder, images_format, classs)
