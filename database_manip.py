import sqlite3

db = sqlite3.connect('venv/student_db')
cursor = db.cursor()
cursor.execute('''
    CREATE TABLE python_programming(id INTEGER PRIMARY KEY, name TEXT, grade INTEGER)
''')
db.commit()

cursor = db.cursor()

grades = [
    (55, 'Carl Davis', 61),
    (66, 'Dennis Fredrickson', 88),
    (77, 'Jane Richards', 78),
    (12, 'Peyton Sawyer', 45),
    (2, 'Lucas Brooke', 99)
]

cursor.executemany('''INSERT INTO python_programming(id, name, grade)
                      VALUES(?,?,?)''', grades)

# Commit changes
db.commit()


# Select records with a grade between 60 and 80

lower_bound = 60
upper_bound = 80
cursor.execute('''SELECT id, name, grade FROM python_programming WHERE grade BETWEEN ? AND ?''', (lower_bound, upper_bound))
python_programming = cursor.fetchall()
print('Here are all the records with a grade between 60 and 80')
print(python_programming)

#update user grade with name
grade = 65
name = 'Carl Davis'
cursor.execute('''UPDATE python_programming SET grade = ? Where name = ?''', (grade, name))
print('Updated Carl\'s grade to 65')

#delete Dennis Fredrickson's row
name = 'Dennis Fredrickson'
cursor.execute('''DELETE FROM python_programming WHERE name = ?''',(name,))
print('Dennis Fredrickson record has been removed from the table.')

db.commit()

# Update grades of people with id less than 55
new_grade = 50
cursor.execute('UPDATE python_programming SET grade = ? WHERE id < 55', (new_grade,))
print('Updated the grade of all people with an id below than 55 to 50')


# Select all records from the table

cursor.execute('''SELECT id, name, grade FROM python_programming''')
python_programming = cursor.fetchall()
print('Here is the whole table:')
print(python_programming)

db.commit()