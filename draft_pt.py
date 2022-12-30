import tkinter
from tkinter import messagebox
from tkinter.ttk import *
from PIL import Image, ImageTk
from module import *
from db_connection import *


def view_info(*args):
    messagebox.showinfo(message='Have a good day')


root = Tk()
root.title("Draft")

listbox = Listbox(
    root,
    height=16,
    font=("Ubuntu Light", 12),
    background='#8F0C25',
    foreground='#DEDEDE',
    relief=FLAT,
    selectbackground='#27A4F3',
    borderwidth=10,
)

for id_name in pokemon_table:
    listbox.insert('end', f'#{str(id_name[0]).zfill(3)} {id_name[1]}')

listbox.grid(column=1, row=1)

listbox.bind('<<ListboxSelect>>', view_info)


root.mainloop()