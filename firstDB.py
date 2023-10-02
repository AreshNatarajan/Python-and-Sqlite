import sqlite3

conn = sqlite3.connect('mydatabase.db')

cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS students (
        id INTEGER PRIMARY KEY,
        name TEXT,
        age INTEGER
    )
''')

name = input("Enter name :")
age = input("Enter age :")


cursor.execute("INSERT INTO students (name, age) VALUES (?, ?)", (name, age))

conn.commit()

cursor.execute("SELECT * FROM students")
students = cursor.fetchall()

for student in students:
    print(f"ID: {student[0]}, Name: {student[1]}, Age: {student[2]}")

conn.close()
