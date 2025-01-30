#!python.exe
import base
import db, session
import cgi

base.start_html()
session_data = session.get_session()

params = cgi.FieldStorage()
student_id = params.getvalue('id')

student = db.get_user_by_userid(student_id)
student_upisni_list = db.get_upisni_list(student_id)

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
    

     for enroll_subject in student_upisni_list:
          subject = db.get_ime_ects(enroll_subject[1])
          print('<tr border = "1px solid black">')
          print('<td border = "1px solid black">') 
          print(subject[0])
          print('</td>')
          print('<td border = "1px solid black">')
          print(subject[1]) 
          print('</td>')
          print('<td border = "1px solid black">')
          print(enroll_subject[2])
          print('</td>')
          print('</tr>') 

          if enroll_subject[2] == "enr":
               count += subject[1]

                

     print('<tr border = "1px solid black">')
     print('<td border = "1px solid black"> Total </td>')
     print('<td border = "1px solid black">')
     print(count)
     print('</td>')
     print('</tr>')

     print('<table>')

list_all()

base.end_html()