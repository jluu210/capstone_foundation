import sqlite3

connection = sqlite3.connect('capstone.db' )

cursor = connection.cursor()

with open("capstone_dummy_data.sql", "r") as sql_file:
    sql_command = sql_file.read()
    cursor.executescript(sql_command)