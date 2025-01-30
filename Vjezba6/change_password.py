#!python.exe
import base
import cgi
import password_hashing
import os
import db
import session

password_error = False
params = cgi.FieldStorage()
if os.environ["REQUEST_METHOD"].upper() == 'POST':
    session_data = session.get_session()
    if params.getvalue("new_pass1") != params.getvalue("new_pass2"):
        password_error = True

    if session_data != {}:
        user = db.get_user_by_userid(session_data["user_id"])
        if not password_error:
            result = password_hashing.change_password(user[1], params.getvalue("password"), params.getvalue("new_pass1"))
            if result:
                print("Location: login.py")
      
   


base.start_html()
print('''
<h2>Promjena lozinke </h2>
Stara lozinka: <input type="password" name="password"><br><br>
Nova lozinka: <input type="password" name="new_pass1"><br><br>
Ponovite novu lozinku: <input type="password" name="new_pass2"><br><br>

<input type="submit" value="Submit">
''')



if os.environ["REQUEST_METHOD"].upper() == 'POST':
    if password_error:
        print('<div>Lozinka i ponovljena lozinka nisu iste!</div>')
    if not result:
        print('<div>Krivo unesena stara lozinka!</div>')

base.end_html()