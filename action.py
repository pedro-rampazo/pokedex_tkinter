from tkinter import *
from db_connection import *
from PIL import Image, ImageTk
from tkinter import messagebox

table = load_table()


def load_items(listbox):
    listbox.delete(0, END)
    for id_name in load_table():
        listbox.insert('end', f'#{str(id_name[0]).zfill(3)} {id_name[1]}')


def show_info(var):
    messagebox.showinfo(message=f"{type(var)}")
