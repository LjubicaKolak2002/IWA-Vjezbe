#!C:\Users\user\AppData\Local\Programs\Python\Python310\python.exe
#C:\ProgramData\Anaconda3\python.exe

import base
import subjects
import cgi
import os
import session
params = cgi.FieldStorage()


if os.environ['REQUEST_METHOD'].upper() == 'POST':
     session.add_to_session(params)
session_data = session.get_session()

    

def print_navigation():
    print('''
    <input type = "submit" name="1" value="1st Year">
    <input type="submit" name="2" value="2nd Year">
    <input type="submit" name="3" value="3rd Year">
    <input type="submit" name="4" value="List all">
    ''')


#ispis jednog predmeta sa odabirom
def display_one_subject(subject, key):

    print('<tr>')
    print('<td>')

    print(subject.get('name'))
    print(subject.get('ects'))

    print('</td>')

    if key in session_data:
        for status in subjects.status_names.values():
            if status == session_data[key]:
                print('<td><input type="radio" name="stat' + key + '" value="'+ status + '" checked>' + status + '</td>')
            else:
                print('<td><input type="radio" name="stat' + key + '" value="'+ status + '">' + status + '</td>')
        
    else:
        for status in subjects.status_names.values():
            if status == 'Not selected':
                print('<td><input type="radio" name="stat' + key + '" value="'+ status + '" checked>' + status + '</td>')
            else:
                print('<td><input type="radio" name="stat' + key + '" value="'+ status + '">' + status + '</td>')
    
    print('</tr>')





#ispis svih predmeta
def display_all_subjects(year):
    for key, subject in subjects.subjects.items():
        if subject.get('year') == year:
            print('<table>')
            display_one_subject(subject, key)
            print('</table>')



base.start_html()
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
     print('''
      <table border = "1px solid black">
           <tr border = "1px solid black">
           <td border = "1px solid black">Subject</td>   
           <td border = "1px solid black">Ects</td>
           <td border = "1px solid black">Status</td>
           </tr>
      ''')

     for key, subject in subjects.subjects.items():

        if key in session_data.keys():
            if session_data[key] == "Enrolled":
                count += subject.get("ects")

            print('<tr border = "1px solid black">')
            print('<td border = "1px solid black">') 
            print(subject.get("name"))
            print('</td>')
            print('<td border = "1px solid black">')
            print(subject.get("ects")) 
            print('</td>')
            print('<td border = "1px solid black">')
            print(session_data[key])
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
print(session_data)
