import tkinter
from tkinter import messagebox
from tkinter.ttk import *
from PIL import Image, ImageTk
from tklib import *
from db_connection import *

pokemon_table = load_table()


def load_items():
    pokemon_list.delete(0, END)
    for id_name in load_table():
        pokemon_list.insert('end', f'#{str(id_name[0]).zfill(3)} {id_name[1]}')


def view_info(*args):
    idx = pokemon_list.curselection()[0]

    display_id = str(pokemon_table[idx][0]).zfill(3)
    display_name = pokemon_table[idx][1]
    display_type = pokemon_table[idx][2]
    display_color = pokemon_table[idx][3]
    display_image = pokemon_table[idx][4]

    pokemon_id.config(text=f'#{display_id}', background=display_color)
    pokemon_name.config(text=f'{display_name}', background=display_color)
    pokemon_type.config(text=f'{display_type}', background=display_color)
    pokemon_image.config(background=display_color)
    pokemon_view.config(background=display_color)

    image = Image.open(display_image)
    image = image.resize((200, 200))
    photo = ImageTk.PhotoImage(image)
    pokemon_image.configure(image=photo)
    pokemon_image.image = photo


def close_window():
    root.quit()


def remove_item():
    poke_obj = pokemon_list.curselection()[0]
    poke_obj = pokemon_list.get(poke_obj)
    poke_obj = poke_obj.split()[1]
    answer = messagebox.askyesno(message='Remove this pokemon?', icon='question', title='Remove')
    if answer:
        query = f"DELETE FROM pokemon WHERE name = '{poke_obj}'"
        db_obj.execute(query)
        mydb.commit()
        load_items()


def add_item():
    window = Tk()
    window.title("Add Pokemon:")
    label = Label(window, text="Add Pokemon:")
    label.grid(column=1, row=1)
    window.mainloop()


"""
INITIALIZING WINDOW
"""


root = Tk()
root.title('Pokedex')


"""
WIDGETS
"""


# HEADER
title_page = Label(
    root,
    text='Pokedex Tkinter',
    font=("Ubuntu", 30),
    foreground='#DE1537'
)

icon_left = get_image(
    root,
    'images/pokeball.png',
    64,
    64
)

icon_right = get_image(
    root,
    'images/pokeball.png',
    64,
    64
)

# POKEMON LIST

pokemon_list = Listbox(
    root,
    height=16,
    font=("Ubuntu Light", 12),
    background='#8F0C25',
    foreground='#DEDEDE',
    relief=FLAT,
    selectbackground='#27A4F3',
    borderwidth=10
)

# POKEMON VIEWER

pokemon_view = tkinter.Frame(
    root,
    width=100,
    height=100
)
pokemon_view.columnconfigure(1, weight=1)
pokemon_view.rowconfigure(1, weight=1)

pokemon_id = Label(
    pokemon_view,
    text='#000',
    font=("Ubuntu Light", 25)
)

image_frame = Frame(
    pokemon_view,
    width=200,
    height=200
)

pokemon_image = get_image(image_frame, 'images/pokemon.png', 200, 200)

pokemon_name = Label(
    pokemon_view,
    text='Pokemon',
    font=("Ubuntu Thin", 25)
)

pokemon_type = Label(
    pokemon_view,
    text='Type',
    font=("Ubuntu Thin", 20)
)


# ACTIONS BUTTONS
add_button = tkinter.Button(
    root,
    text='Add',
    bg='#4CA459',
    foreground='#FFF',
    font=("Ubuntu Light", 14),
    height=1,
    relief=FLAT,
    width=8,
    activeforeground='#4CA459',
    command=add_item
)

edit_button = tkinter.Button(
    root,
    text='Edit',
    bg='#27A4F3',
    foreground='#FFF',
    font=("Ubuntu Light", 14),
    height=1,
    relief=FLAT,
    width=8,
    activeforeground='#27A4F3'
)

exit_button = tkinter.Button(
    root,
    text='Exit',
    background='#363636',
    foreground='#FFFFFF',
    font=("Ubuntu Light", 14),
    height=1,
    relief=FLAT,
    width=8,
    activeforeground="#363636",
    command=close_window
)

remove_button = tkinter.Button(
    root,
    text="Remove",
    background='#DE1537',
    foreground='#FFFFFF',
    font=("Ubuntu Light", 14),
    height=1,
    relief=FLAT,
    width=8,
    activeforeground="#DE1537",
    command=remove_item
)


"""
STYLE
"""


dark_red = Style()
dark_red.configure('DarkRed.TFrame', background='#8F0C25')


"""
PLACE
"""


title_page.grid(
    column=2,
    row=1,
    columnspan=2
)

icon_left.grid(
    column=1,
    row=1,
    pady=10,
    padx=100
)

icon_right.grid(
    column=4,
    row=1,
    pady=10,
    padx=100
)

pokemon_list.grid(
    column=1,
    row=2,
    sticky='nsew',
    columnspan=2,
    padx=10,
    pady=5
)

pokemon_view.grid(
    column=3,
    row=2,
    sticky='nsew',
    columnspan=4,
    padx=10,
    pady=5
)

pokemon_id.grid(
    column=1,
    row=1,
    sticky='W',
    pady=10,
    padx=10
)

image_frame.grid(
    column=1,
    row=2
)

pokemon_image.grid(
    column=1,
    row=1
)

pokemon_name.grid(
    column=1,
    row=3,
    pady=5
)

pokemon_type.grid(
    column=1,
    row=4,
    sticky='W',
    pady=10,
    padx=10
)

add_button.grid(
    column=1,
    row=3,
    sticky="W",
    padx=10,
    pady=5
)

edit_button.grid(
    column=1,
    row=3,
    sticky="E",
    padx=10,
    pady=5
)

exit_button.grid(
    column=4,
    row=3,
    sticky="E",
    padx=10,
    pady=5
)

remove_button.grid(
    column=4,
    row=3,
    sticky="W",
    padx=10,
    pady=5
)


"""
FUNCTIONALITIES
"""


load_items()

pokemon_list.bind('<<ListboxSelect>>', view_info)

root.mainloop()
