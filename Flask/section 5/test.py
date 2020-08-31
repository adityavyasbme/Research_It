import sqlite3

connection = sqlite3.connect('data.db')

cursor = connection.cursor()

create_table = "CREATE TABLE users (ID int, Username text, Password text)"
cursor.execute(create_table)

user = (1,'jose','asdf')
insert_query = "INSERT INTO users VALUES (?,?,?)"
cursor.execute(insert_query,user)

users = [
    (2,'aditya','asdf'),
    (3,'sam','xyz')
]
cursor.executemany(insert_query,users)

select_query = "SELECT * FROM users"

for row in cursor.execute(select_query):
    print(row)

connection.commit()

connection.close()


