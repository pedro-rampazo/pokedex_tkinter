import os.path
from tkinter import *
from tklib import *
import tkinter
from tkinter import messagebox, colorchooser, filedialog
from db_connection import *
from main_window import *


class AddItemWindow:
    def __init__(self, master):
        self.master = master
        master.title("Add")

        # HEADER

        self.title_page = Label(
            master,
            text="Add Pokemon",
            font=("Ubuntu", 20),
            foreground="#DE1537"
        )
        self.title_page.grid(
            column=2,
            row=1,
            columnspan=2,
            pady=15
        )

        # LABELS

        self.id_label = Label(
            master,
            text="Pokemon Number:",
            font=("Ubuntu Thin", 12)
        )
        self.id_label.grid(
            column=1,
            row=2,
            pady=10,
            padx=5
        )

        self.name_label = Label(
            master,
            text="Name:",
            font=("Ubuntu Thin", 12),
        )
        self.name_label.grid(
            column=1,
            row=3,
            pady=10,
            padx=5
        )

        self.type_label = Label(
            master,
            text="Type:",
            font=("Ubuntu Thin", 12)
        )
        self.type_label.grid(
            column=1,
            row=4,
            pady=10,
            padx=5
        )

        self.color_label = Label(
            master,
            text="Color:",
            font=("Ubuntu Thin", 12)
        )
        self.color_label.grid(
            column=1,
            row=5,
            pady=10,
            padx=5
        )

        self.image_label = Label(
            master,
            text="Image:",
            font=("Ubuntu Thin", 12)
        )
        self.image_label.grid(
            column=1,
            row=6,
            pady=10,
            padx=5
        )

        self.color_strvar = StringVar()
        self.color_selected = Label(
            master,
            textvariable=self.color_strvar,
            font=("Ubuntu Light", 12)
        )
        self.color_selected.grid(
            column=2,
            row=5,
            pady=10,
            padx=5,
            columnspan=2
        )

        self.image_strvar = StringVar()
        self.image_selected = Label(
            master,
            textvariable=self.image_strvar,
            font=("Ubuntu Light", 12)
        )
        self.image_selected.grid(
            column=2,
            row=6,
            pady=10,
            padx=5,
            columnspan=2
        )

        # ENTRYS

        self.id_intvar = IntVar()
        self.id_entry = Entry(
            master,
            textvariable=self.id_intvar,
            font=("Ubuntu Light", 12)
        )
        self.id_entry.grid(
            column=2,
            row=2,
            pady=10,
            padx=10,
            columnspan=4,
            sticky="WE"
        )

        self.name_strvar = StringVar()
        self.name_entry = Entry(
            master,
            textvariable=self.name_strvar,
            font=("Ubuntu Light", 12)
        )
        self.name_entry.grid(
            column=2,
            row=3,
            pady=10,
            padx=10,
            columnspan=4,
            sticky="WE"
        )

        self.type_strvar = StringVar()
        self.type_entry = Entry(
            master,
            textvariable=self.type_strvar,
            font=("Ubuntu Light", 12)
        )
        self.type_entry.grid(
            column=2,
            row=4,
            pady=10,
            padx=10,
            columnspan=4,
            sticky="WE"
        )

        # BUTTONS

        self.color_button = tkinter.Button(
            master,
            text="Select color...",
            background="#DEDEDE",
            font=("Ubuntu Light", 12),
            command=self.select_color
        )
        self.color_button.grid(
            column=4,
            row=5,
            pady=10,
            padx=5,
            sticky="WE"
        )

        self.image_button = tkinter.Button(
            master,
            text="Select image...",
            background="#DEDEDE",
            font=("Ubuntu Light", 12),
            command=self.select_image
        )
        self.image_button.grid(
            column=4,
            row=6,
            pady=10,
            padx=5,
            sticky="WE"
        )

        self.save_button = tkinter.Button(
            master,
            text="Save",
            background="#27A4F3",
            font=("Ubuntu Light", 12),
            foreground="#DEDEDE",
            relief=FLAT,
            command=self.register
        )
        self.save_button.grid(
            column=3,
            row=7,
            pady=10,
            sticky="WE"
        )

        self.quit_button = tkinter.Button(
            master,
            text="Quit",
            background="#DE1537",
            font=("Ubuntu Light", 12),
            foreground="#DEDEDE",
            relief=FLAT,
            command=self.quit_confirmation
        )
        self.quit_button.grid(
            column=4,
            row=7,
            pady=10,
            padx=5,
            sticky="WE"
        )

    def quit_confirmation(self):
        answer = messagebox.askyesno(message="Are you sure you want to leave?", icon="question", title="Quit?")
        if answer:
            self.master.destroy()

    def select_color(self):
        answer = colorchooser.askcolor(initialcolor="#000000")[1]
        self.color_strvar.set(str(answer))

    def select_image(self):
        answer = filedialog.askopenfilename(
            filetypes=[("Image Files", "*.png")],
            initialdir="/home/pedro/Development/git_space/pokedex_tkinter/images"
        )
        answer = format_path(answer)
        self.image_strvar.set(str(answer))

    def register(self):
        info_list = [
            self.id_intvar.get(),
            self.name_strvar.get(),
            self.type_strvar.get(),
            self.color_strvar.get(),
            self.image_strvar.get()
        ]

        for item in info_list:
            if not item:
                return messagebox.showinfo(message=f"Error: empty fields")

        query = f"INSERT INTO pokemon VALUES (" \
                f"{info_list[0]}, " \
                f"{info_list[1]}, " \
                f"{info_list[2]}, " \
                f"{info_list[3]}, " \
                f"{info_list[4]})"
        db_obj.execute(query)
        mydb.commit()
        self.master.destroy()
