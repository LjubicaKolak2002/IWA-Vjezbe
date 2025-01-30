#!C:\ProgramData\Anaconda3\python.exe

import base
import subjects
import cgi
import os
import session
import db
params = cgi.FieldStorage()


if os.environ['REQUEST_METHOD'].upper() == 'POST':
     session.add_to_session(params)
session_data = session.get_session()

if session_data != {}:
    user = db.get_user_by_userid(session_data["user_id"])
    if not user:
        print("Location:login.py")
else:
    print("Location:login.py")
       
base.start_html()
if user:
    print('<div>Hej ' + user[1] + '!' + '</div>')


    

def print_navigation():
    print('''
    <input type = "submit" name="1" value="1st Year">
    <input type="submit" name="2" value="2nd Year">
    <input type="submit" name="3" value="3rd Year">
    <input type="submit" name="4" value="List all">
    ''')

def display_one_subject(subject):

    print('<tr>')
    print('<td>')
    print(subject[2]) #naziv predmeta
    print(subject[3]) #ects bodovi
    print('</td>')

    if subject[1] in session_data:
        for status in subjects.status_names.values():
            if status == session_data[subject[1]]:
                print('<td><input type="radio" name="stat' + subject[1] + '" value="'+ status + '" checked>' + status + '</td>')
            else:
                print('<td><input type="radio" name="stat' + subject[1] + '" value="'+ status + '">' + status + '</td>')
        
    else:
        for status in subjects.status_names.values():
            if status == 'Not selected':
                print('<td><input type="radio" name="stat' + subject[1] + '" value="'+ status + '" checked>' + status + '</td>')
            else:
                print('<td><input type="radio" name="stat' + subject[1] + '" value="'+ status + '">' + status + '</td>')
    
    print('</tr>')


def display_all_subjects(year):
    subjects = db.get_subjects(year)
    for subject in subjects:
        print('<table>')
        display_one_subject(subject)
        print('</table>')


print('<br>')
print_navigation()
print('<br>')


def print_all_html():
    for key, year in subjects.year_names.items():
        if params.getvalue(str(key)):
            print('''
            <table>
            <tr>
            <td>'''+ year + '''</td>
            </tr>

            <tr>
            <td>Subject</td>
            <td>Ects</td>
            <td>Status</td>
            </tr>
            </table>
            ''')
            display_all_subjects(key)
        
    if params.getvalue("4"):
      list_all()


def list_all():
     count = 0
     subjects_data = db.get_all_of_subjects()
     print(subjects)

     print('''
      <table border = "1px solid black">
           <tr border = "1px solid black">
           <td border = "1px solid black">Subject</td>   
           <td border = "1px solid black">Ects</td>
           <td border = "1px solid black">Status</td>
           </tr>
      ''')
    

     for subject in subjects_data:
        if subject[1] in session_data.keys():
            if session_data[subject[1]] == "Enrolled":
                count += subject[3]

            print('<tr border = "1px solid black">')
            print('<td border = "1px solid black">') 
            print(subject[2])
            print('</td>')
            print('<td border = "1px solid black">')
            print(subject[3]) 
            print('</td>')
            print('<td border = "1px solid black">')
            print(session_data[subject[1]])
            print('</td>')
            print('</tr>')     

     print('<tr border = "1px solid black">')
     print('<td border = "1px solid black"> Total </td>')
     print('<td border = "1px solid black">')
     print(count)
     print('</td>')
     print('</tr>')

     print('<table>')


print_all_html()
base.end_html()
print('<br>')
print('''<br>
    <button><a href="logout.py"> Logout</a></button>
    <button><a href="change_password.py"> Promjena lozinke</a></button>
    <br>
''')
print(session_data)

