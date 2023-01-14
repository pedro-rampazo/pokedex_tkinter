import tkinter

from tklib import *
from tkinter.ttk import *
from tkinter import *
from tkinter import messagebox
from db_connection import *
from additem_window import *
from PIL import Image, ImageTk


class MainWindow:
    def __init__(self, master):
        self.master = master
        master.title("Pokedex")

        # DATABASE OBJECT

        self.pokemon_table = load_table()

        # HEADER

        self.title_page = Label(
            master,
            text="Pokedex Tkinter",
            font=("Ubuntu", 30),
            foreground="#DE1537"
        )
        self.title_page.grid(
            column=2,
            row=1,
            columnspan=2
        )

        self.icon_left = get_image(
            master,
            'images/pokeball.png',
            64,
            64
        )
        self.icon_left.grid(
            column=1,
            row=1,
            pady=10,
            padx=100
        )

        self.icon_right = get_image(
            master,
            'images/pokeball.png',
            64,
            64
        )
        self.icon_right.grid(
            column=4,
            row=1,
            pady=10,
            padx=100
        )

        # POKEMON LIST

        self.pokemon_list = Listbox(
            master,
            height=16,
            font=("Ubuntu Light", 12),
            background='#8F0C25',
            foreground='#DEDEDE',
            relief=FLAT,
            selectbackground='#27A4F3',
            borderwidth=10
        )
        self.pokemon_list.grid(
            column=1,
            row=2,
            sticky='nsew',
            columnspan=2,
            padx=10,
            pady=5
        )
        self.load_items()
        self.pokemon_list.bind('<<ListboxSelect>>', self.view_info)

        # POKEMON VIEWER

        self.pokemon_view = tkinter.Frame(
            master,
            width=100,
            height=100
        )
        self.pokemon_view.grid(
            column=3,
            row=2,
            sticky='nsew',
            columnspan=4,
            padx=10,
            pady=5
        )
        self.pokemon_view.columnconfigure(1, weight=1)
        self.pokemon_view.rowconfigure(1, weight=1)

        self.pokemon_id = tkinter.Label(
            self.pokemon_view,
            text='#000',
            font=("Ubuntu Light", 25)
        )
        self.pokemon_id.grid(
            column=1,
            row=1,
            sticky='W',
            pady=10,
            padx=10
        )

        self.image_frame = tkinter.Frame(
            self.pokemon_view,
            width=200,
            height=200
        )
        self.image_frame.grid(
            column=1,
            row=2
        )

        self.pokemon_image = get_image(
            self.image_frame,
            'images/pokemon.png',
            200,
            200
        )
        self.pokemon_image.grid(
            column=1,
            row=1
        )

        self.pokemon_name = tkinter.Label(
            self.pokemon_view,
            text='Pokemon',
            font=("Ubuntu Thin", 25)
        )
        self.pokemon_name.grid(
            column=1,
            row=3,
            pady=5
        )

        self.pokemon_type = tkinter.Label(
            self.pokemon_view,
            text='Type',
            font=("Ubuntu Thin", 20)
        )
        self.pokemon_type.grid(
            column=1,
            row=4,
            sticky='W',
            pady=10,
            padx=10
        )

        # ACTIONS BUTTONS

        self.add_button = tkinter.Button(
            master,
            text='Add',
            background='#4CA459',
            foreground='#FFF',
            font=("Ubuntu Light", 14),
            height=1,
            relief=FLAT,
            width=8,
            activeforeground='#4CA459',
            command=self.add_item
        )
        self.add_button.grid(
            column=1,
            row=3,
            sticky="W",
            padx=10,
            pady=5
        )

        self.edit_button = tkinter.Button(
            master,
            text='Edit',
            bg='#27A4F3',
            foreground='#FFF',
            font=("Ubuntu Light", 14),
            height=1,
            relief=FLAT,
            width=8,
            activeforeground='#27A4F3'
        )
        self.edit_button.grid(
            column=1,
            row=3,
            sticky="E",
            padx=10,
            pady=5
        )

        self.exit_button = tkinter.Button(
            master,
            text='Exit',
            bg='#363636',
            foreground='#FFFFFF',
            font=("Ubuntu Light", 14),
            height=1,
            relief=FLAT,
            width=8,
            activeforeground="#363636",
            command=master.destroy
        )
        self.exit_button.grid(
            column=4,
            row=3,
            sticky="E",
            padx=10,
            pady=5
        )

        self.remove_button = tkinter.Button(
            master,
            text="Remove",
            bg='#DE1537',
            foreground='#FFFFFF',
            font=("Ubuntu Light", 14),
            height=1,
            relief=FLAT,
            width=8,
            activeforeground="#DE1537",
            command=self.remove_item
        )
        self.remove_button.grid(
            column=4,
            row=3,
            sticky="W",
            padx=10,
            pady=5
        )

    def load_items(self):
        self.pokemon_list.delete(0, END)
        for id_name in load_table():
            self.pokemon_list.insert('end', f"#{str(id_name[0]).zfill(3)} {id_name[1]}")

    def remove_item(self):
        poke_obj = self.pokemon_list.curselection()[0]
        poke_obj = self.pokemon_list.get(poke_obj)
        poke_obj = poke_obj.split()[1]
        answer = messagebox.askyesno(message="Remove this pokemon?", icon="question", title="Remove")
        if answer:
            query = f"DELETE FROM pokemon WHERE name = '{poke_obj}'"
            db_obj.execute(query)
            mydb.commit()
            self.load_items()

    def view_info(self, *args):
        idx = self.pokemon_list.curselection()[0]

        display_id = str(self.pokemon_table[idx][0]).zfill(3)
        display_name = self.pokemon_table[idx][1]
        display_type = self.pokemon_table[idx][2]
        display_color = self.pokemon_table[idx][3]
        display_image = self.pokemon_table[idx][4]

        self.pokemon_id.config(text=f"#{display_id}", background=display_color)
        self.pokemon_name.config(text=f"{display_name}", background=display_color)
        self.pokemon_type.config(text=f"{display_type}", background=display_color)
        self.pokemon_image.config(background=display_color)
        self.pokemon_view.config(background=display_color)

        image = Image.open(display_image)
        image = image.resize((200, 200))
        photo = ImageTk.PhotoImage(image)
        self.pokemon_image.configure(image=photo)
        self.pokemon_image.image = photo

    def add_item(self):
        new_window = tkinter.Toplevel()
        AddItemWindow(new_window)
        self.load_items()
        new_window.mainloop()
