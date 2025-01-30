#!C:\ProgramData\Anaconda3\python.exe
import os
import db
import cgi
import base
import session
params = cgi.FieldStorage()

if os.environ["REQUEST_METHOD"].upper() == 'POST':
    result, user_id = db.login(params.getvalue("username"), params.getvalue("pass"))
    if result:
        session.add_to_session2({"user_id": user_id})
        print("Location:display.py")
   

base.start_html()
print('''
<h2>Prijava korisnika</h2><br>
    Korisnicko ime: <input type="text" name="username" value="" placeholder="Upisite svoje ime"><br><br>
    Lozinka: <input type="password" name="pass"><br><br>
            
    <input type="submit" value="Login">
''')

base.end_html()

if os.environ["REQUEST_METHOD"].upper() == 'POST' and not result:
    print('<div>Kriva potvrda lozinke ili korisnickog imena!</div>')

