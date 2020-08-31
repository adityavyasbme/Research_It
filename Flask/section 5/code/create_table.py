import sqlite3

connection = sqlite3.connect('data.db')

cursor = connection.cursor()

create_table = "CREATE TABLE IF NOT EXISTS users (ID INTEGER PRIMARY KEY,Username text,Password text)"

cursor.execute(create_table)

create_table = "CREATE TABLE IF NOT EXISTS items (name text,price real)"
cursor.execute(create_table)


connection.commit()

connection.close()

 