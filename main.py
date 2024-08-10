import sqlite3

db = sqlite3.connect('university.db')
db.execute('''
CREATE TABLE IF NOT EXISTS students(
        student_id INTEGER PRIMARY KEY AUTOINCREMENT,
        name VARCHAR(63),
        age INTEGER,
        major VARCHAR(63)) ''')

db.execute('''
CREATE TABLE IF NOT EXISTS course(
        course_id INTEGER PRIMARY KEY AUTOINCREMENT,
        course_name VARCHAR(63),
        instructor VARCHAR(63)) ''')

db.execute('''
CREATE TABLE IF NOT EXISTS student_course(
        student_id INTEGER REFERENCES student(student_id),
        course_id INTEGER REFERENCES course(course_id),
        PRIMARY KEY(student_id, course_id)) ''')

def add_student(db):
    name = input("name: ")
    age = int(input('age: '))
    major = input('major: ')

    db.execute(f'''
        INSERT INTO students(name, age, major) VALUES {name, age, major}
    ''')
    db.commit()
    print('студента успішно додано')

def add_courses(db):
    name = input("name: ")
    instructor = input('instructors: ')

    db.execute(f'''
        INSERT INTO course(course_name, instructor) VALUES {name, instructor}
    ''')
    db.commit()
    print('курс успішно додано')

def get_students(db):
    student = db.execute('''
    SELECT * FROM students
    ''')
    for s in student:
        print(s)

def get_courses(db):
    courses = db.execute('''
    SELECT * FROM course
    ''')
    for c in courses:
        print(c)

def add_student_to_coures(db):
    student_id = input("student_id: ")
    course_id = input('course_id: ')

    db.execute(f'''
        INSERT INTO student_course(student_id, course_id) VALUES {student_id, course_id}
    ''')
    db.commit()
    print('курс успішно привязвно до студента')

def get_students_on_course(db):
    course_id = int(input('course_id: '))   

    student_on_course = db.execute(f'''
    SELECT * FROM students 
    JOIN student_course ON students.student_id = student_course.student_id
    WHERE student_course.course_id = {course_id}
    ''')
    for s in student_on_course:
        print(s)

while True:
    print("\n1. Додати нового студента")
    print("2. Додати новий курс")
    print("3. Показати список студентів")
    print("4. Показати список курсів")
    print("5. Зареєструвати студента на курс")
    print("6. Показати студентів на конкретному курсі")
    print("7. Оновити інформацію студента")
    print("8. Вийти")

    choice = input("Оберіть опцію (1-7): ")
    
    if choice == "1":
        add_student(db)

    elif choice == '2':
        add_courses(db)

    elif choice == '3':
        get_students(db)

    elif choice == '4':
        get_courses(db)

    elif choice == '5':
        add_student_to_coures(db)

    elif choice == '5':
        get_students_on_course(db)

    elif choice == '8':
        break
