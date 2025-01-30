#!python.exe

import base
import db
import session
session_data = session.get_session()
user_role = db.get_role(session_data)

base.start_html()
if user_role[0] == 'student':
    print('<div>Nemate pravo pristupa!</div>')

else:
    print('<h3>Popis studenata</h3>')
    students = db.get_student_by_role()

    for student in students:
        print(student[1])
        print('<a href="upisni_list.py/?id=' + str(student[0]) + '">Upisni list</a>')
        print('<br>')

    base.end_html()

