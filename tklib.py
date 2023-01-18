from tkinter import *
from tkinter.ttk import *
from PIL import Image, ImageTk
from tkinter import messagebox


def get_image(parent, image_path, width, height):
    image = Image.open(image_path)
    image = image.resize((width, height))
    photo = ImageTk.PhotoImage(image)
    label = Label(parent, image=photo)
    label.image = photo
    return label


def format_path(filepath):
    filepath = filepath.split("/")
    return f"{filepath[-2]}/{filepath[-1]}"


def check_fields(*args):
    for item in args:
        if not item:
            return
    return args
