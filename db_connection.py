import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="P*e*d*r*o*16541815",
    database="pokedex_tkinter"
)

db_obj = mydb.cursor()


def load_table():
    db_obj.execute("SELECT * FROM pokemon")
    pokemon_table = db_obj.fetchall()
    return pokemon_table
