from tkinter import *
from tkinter.ttk import *
from PIL import Image, ImageTk


def get_image(parent, image_path, width, height):
    image = Image.open(image_path)
    image = image.resize((width, height))
    photo = ImageTk.PhotoImage(image)
    label = Label(parent, image=photo)
    label.image = photo
    return label
