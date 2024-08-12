import sqlite3

db = sqlite3.connect('university2.db')

db.execute('''
CREATE TABLE IF NOT EXISTS students(
        student_id INTEGER PRIMARY KEY AUTOINCREMENT,
        name VARCHAR(63),
        age INTEGER) ''')

db.execute('''
CREATE TABLE IF NOT EXISTS grades(
        student_id INTEGER PRIMARY KEY AUTOINCREMENT,
        subject VARCHAR(63),
        grade INTEGER)''')

info = db.execute('''
SELECT AVG(grade) FROM grades 
        INNER JOIN students ON students.student_id = grades.student_id 
        WHERE students.age < 20 
        GROUP BY grades.subject

''')
