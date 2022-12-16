import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="P*e*d*r*o*16541815",
    database="pokedex_tkinter"
)

db_obj = mydb.cursor()
