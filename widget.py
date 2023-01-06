import tkinter
from tkinter.ttk import *
from tkinter import *
from tklib import *
from action import *


def widget(root_window):

    # HEADER

    title_page = Label(
        root_window,
        text='Pokedex Tkinter',
        font=("Ubuntu", 30),
        foreground='#DE1537'
    )
    title_page.grid(
        column=2,
        row=1,
        columnspan=2
    )

    icon_left = get_image(
        root_window,
        'images/pokeball.png',
        64,
        64
    )
    icon_left.grid(
        column=1,
        row=1,
        pady=10,
        padx=100
    )

    icon_right = get_image(
        root_window,
        'images/pokeball.png',
        64,
        64
    )
    icon_right.grid(
        column=4,
        row=1,
        pady=10,
        padx=100
    )

    # POKEMON LIST

    pokemon_list = Listbox(
        root_window,
        height=16,
        font=("Ubuntu Light", 12),
        background='#8F0C25',
        foreground='#DEDEDE',
        relief=FLAT,
        selectbackground='#27A4F3',
        borderwidth=10
    )
    pokemon_list.grid(
        column=1,
        row=2,
        sticky='nsew',
        columnspan=2,
        padx=10,
        pady=5
    )
    load_items(pokemon_list)

    # POKEMON VIEWER

    pokemon_view = tkinter.Frame(
        root_window,
        width=100,
        height=100
    )
    pokemon_view.grid(
        column=3,
        row=2,
        sticky='nsew',
        columnspan=4,
        padx=10,
        pady=5
    )
    pokemon_view.columnconfigure(1, weight=1)
    pokemon_view.rowconfigure(1, weight=1)

    pokemon_id = Label(
        pokemon_view,
        text='#000',
        font=("Ubuntu Light", 25)
    )
    pokemon_id.grid(
        column=1,
        row=1,
        sticky='W',
        pady=10,
        padx=10
    )

    image_frame = Frame(
        pokemon_view,
        width=200,
        height=200
    )
    image_frame.grid(
        column=1,
        row=2
    )

    pokemon_image = get_image(
        image_frame,
        'images/pokemon.png',
        200,
        200
    )
    pokemon_image.grid(
        column=1,
        row=1
    )

    pokemon_name = Label(
        pokemon_view,
        text='Pokemon',
        font=("Ubuntu Thin", 25)
    )
    pokemon_name.grid(
        column=1,
        row=3,
        pady=5
    )

    pokemon_type = Label(
        pokemon_view,
        text='Type',
        font=("Ubuntu Thin", 20)
    )
    pokemon_type.grid(
        column=1,
        row=4,
        sticky='W',
        pady=10,
        padx=10
    )

    # BUTTONS

    add_button = tkinter.Button(
        root_window,
        text='Add',
        bg='#4CA459',
        foreground='#FFF',
        font=("Ubuntu Light", 14),
        height=1,
        relief=FLAT,
        width=8,
        activeforeground='#4CA459'
        # command=add_item
    )
    add_button.grid(
        column=1,
        row=3,
        sticky="W",
        padx=10,
        pady=5
    )

    edit_button = tkinter.Button(
        root_window,
        text='Edit',
        bg='#27A4F3',
        foreground='#FFF',
        font=("Ubuntu Light", 14),
        height=1,
        relief=FLAT,
        width=8,
        activeforeground='#27A4F3'
    )
    edit_button.grid(
        column=1,
        row=3,
        sticky="E",
        padx=10,
        pady=5
    )

    exit_button = tkinter.Button(
        root_window,
        text='Exit',
        background='#363636',
        foreground='#FFFFFF',
        font=("Ubuntu Light", 14),
        height=1,
        relief=FLAT,
        width=8,
        activeforeground="#363636",
        command=lambda: show_info(root_window)
    )
    exit_button.grid(
        column=4,
        row=3,
        sticky="E",
        padx=10,
        pady=5
    )

    remove_button = tkinter.Button(
        root_window,
        text="Remove",
        background='#DE1537',
        foreground='#FFFFFF',
        font=("Ubuntu Light", 14),
        height=1,
        relief=FLAT,
        width=8,
        activeforeground="#DE1537"
        # command=remove_item(pokemon_list)
    )
    remove_button.grid(
        column=4,
        row=3,
        sticky="W",
        padx=10,
        pady=5
    )
