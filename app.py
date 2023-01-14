from tkinter import *
from main_window import *


class App:
    def __init__(self):
        root = Tk()
        MainWindow(root)
        # AddItemWindow(root)
        root.mainloop()


if __name__ == "__main__":
    App()
