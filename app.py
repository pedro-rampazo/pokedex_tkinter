import tkinter
from widget import widget


class App(tkinter.Tk):
    def __init__(self):
        root = super().__init__()
        self.title('Pokedex')

        widget(root)


if __name__ == "__main__":
    app = App()
    app.mainloop()
