import tkinter as tk
from tkinter import filedialog


def select_dir(debug=False):

    root = tk.Tk()
    root.withdraw()

    selected_dir = filedialog.askdirectory()

    if debug:
        print("Selected dataset:", selected_dir)

    return selected_dir


def select_file(base, debug=False):

    root = tk.Tk()
    root.withdraw()

    select_file = filedialog.askopenfile(initialdir=base)

    if debug:
        print("Selected dataset:", select_file)

    return select_file
