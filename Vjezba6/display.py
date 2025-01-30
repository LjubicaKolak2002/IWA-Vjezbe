#!python.exe

from requests import request
import base
import subjects
import cgi, os
import session
import db
params = cgi.FieldStorage()

session_data = session.get_session()

subjects_data = db.get_all_of_subjects()
upisni_list = db.get_upisni_list(session_data)

if session_data != {}:
    user = db.get_user_by_userid(session_data)
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
    ''')

def display_one_subject(subject):

    
    print('<tr>')
    print('<td>')
    print(subject[2]) #naziv predmeta
    print(subject[3]) #ects bodovi
    print('</td>')

    flag = True
    for enroll_subject in upisni_list:
        if enroll_subject[1] == subject[0] and enroll_subject[2] == 'enr':
            print('<td><input type="radio" name="' + str(subject[0]) + '" value="'+ enroll_subject[2] + '" checked>' + 'Enrolled' + '</td>')
            print('<td><input type="radio" name="' + str(subject[0]) + '" value="'+ 'pas' + '">' + 'Pass' + '</td>')
            print('<td><input type="radio" name="' + str(subject[0]) + '" value="'+ 'not' + '">' + 'Not Selected' + '</td>')
            db.update_upisni_list(enroll_subject[0], enroll_subject[1], enroll_subject[2])
            flag = False
            break

        elif enroll_subject[1] == subject[0] and enroll_subject[2] == 'pas':
            print('<td><input type="radio" name="' + str(subject[0]) + '" value="'+ enroll_subject[2] + '" checked>' + 'Passed' + '</td>')
            print('<td><input type="radio" name="' + str(subject[0]) + '" value="'+ 'enr' + '">' + 'Enrolled' + '</td>')
            print('<td><input type="radio" name="' + str(subject[0]) + '" value="'+ 'not' + '">' + 'Not Selected' + '</td>')
            db.update_upisni_list(enroll_subject[0], enroll_subject[1], enroll_subject[2])
            flag = False
            break

        elif enroll_subject[1] == subject[0] and enroll_subject[2] == 'not':
            print('<td><input type="radio" name="' + str(subject[0]) + '" value="'+ 'pas' + '">' + 'Passed' + '</td>')
            print('<td><input type="radio" name="' + str(subject[0]) + '" value="'+ 'enr' + '">' + 'Enrolled' + '</td>')
            print('<td><input type="radio" name="' + str(subject[0]) + '" value="'+ enroll_subject[2] + '" checked>' + 'Not Selected' + '</td>')
            db.update_upisni_list(enroll_subject[0], enroll_subject[1], enroll_subject[2])
            flag = False
            break

    if flag:
        print('<td><input type="radio" name="' + str(subject[0]) + '" value="'+ 'enr' + '" variable = sub>' + 'Enrolled' + '</td>')
        print('<td><input type="radio" name="' + str(subject[0]) + '" value="'+ 'pas' + '"  variable = sub>' + 'Pass' + '</td>')
        print('<td><input type="radio" name="' + str(subject[0]) + '" value="'+ 'not' + '"  variable = sub checked>' + 'Not Selected' + '</td>')
      
        db.insert_upisni_list(session_data, subject[0], "not")
    
        
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
        
   
print_all_html()


base.end_html()
print('<br>')
print('''<br>
    <button><a href="logout.py"> Logout</a></button>
    <button><a href="change_password.py"> Promjena lozinke</a></button>
    <button><a href="popis_studenata.py"> Popis studenata</a></button>
    <br>
''')
