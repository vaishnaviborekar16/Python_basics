#Write a Python script to insert a new record into a database table using SQLite3.
import sqlite3

conn = sqlite3.connect('mydatabase.db')
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        age INTEGER
    )
''')

cursor.execute("INSERT INTO users (name, age) VALUES (?, ?)", ('John Doe', 30))
conn.commit()
conn.close()
