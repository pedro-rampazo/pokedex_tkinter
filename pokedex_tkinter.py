from tkinter import *
from tkinter.ttk import *

root = Tk()
root.title('Pokedex')
root.configure(width=683, height=384)

s = Style()
s.configure('My.TFrame', background='dark blue')

mail1 = Frame(root, style='My.TFrame')
mail1.place(height=50, width=600)
mail1.config()
root.mainloop()
