import tkinter
from tkinter.ttk import *
from PIL import Image, ImageTk
from module import *
from db_connection import *

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

pokemon_view = Frame(
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
    activeforeground='#4CA459'
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
    activeforeground="#363636"
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
    activeforeground="#DE1537"
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

for id_name in pokemon_table:
    pokemon_list.insert('end', f'#{str(id_name[0]).zfill(3)} {id_name[1]}')

root.mainloop()
