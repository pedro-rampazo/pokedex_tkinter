#! /home/pedro/Development/venv/tkinter_venv/bin/python

from tkinter import *
from main_window import *


class App:
    def __init__(self):
        self.root = Tk()
        MainWindow(self.root)
        # AddItemWindow(root)
        self.root.mainloop()


if __name__ == "__main__":
    App()
