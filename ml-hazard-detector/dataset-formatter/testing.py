import cv2
import matplotlib.pyplot as plt
import random
import os


def render_random(annotated_dataset_path):

    while True:

        sample_index = random.randrange(
            0, len(os.listdir(annotated_dataset_path)) / 2, 2
        )

        image_path = rf"{annotated_dataset_path}/element_{sample_index}_picture.png"
        text_file_path = (
            rf"{annotated_dataset_path}/element_{sample_index}_annotations_.txt"
        )

        image = cv2.imread(image_path)
        text_file = open(text_file_path, "r")
        dh, dw, _ = image.shape

        data = text_file.readlines()

        for dt in data:

            # Split string to float
            _, x, y, w, h = map(float, dt.split(" "))

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

            # cv2.rectangle(img, (l, t), (r, b), (0, 0, 255), 1)
            cv2.rectangle(image, (l, t), (r, b), (0, 0, 255), 1)

        plt.imshow(image)
        plt.show()
