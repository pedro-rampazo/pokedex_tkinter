import tkinter
from tkinter.ttk import *
from PIL import Image, ImageTk
from module import *

root = Tk()
root.title('Pokedex')

# WIDGETS

title_page = Label(
    root,
    text='Pokedex Tkinter',
    font=("Ubuntu", 30),
    foreground='#DE1537'
)

icon_left = get_image(root, 'images/pokeball.png')
icon_right = get_image(root, 'images/pokeball.png')

pokemon_list = Listbox(
    root,
    height=16,
    font=("Ubuntu", 12),
    background='#8F0C25',
    foreground='#DEDEDE',
    relief=FLAT,
    selectbackground='#27A4F3',
    borderwidth=10
)

pokemon_view = Frame(
    root,
    width=100,
    height=100,
    style='LightBlue.TFrame'
)

icon_list = get_image(pokemon_list, 'images/pokeball.png')

# STYLE
dark_red = Style()
dark_red.configure('DarkRed.TFrame', background='#8F0C25')

light_blue = Style()
light_blue.configure('LightBlue.TFrame', background='#27A4F3')

# PLACE
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

for x in range(100):
    pokemon_list.insert('end', f'Line {x} of 100')


root.mainloop()
