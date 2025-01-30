#!python.exe

import base
import cgi
import os
import db
params = cgi.FieldStorage()

username_error = False
mail_error = False
password_error = False

if os.environ["REQUEST_METHOD"].upper() == 'POST':
    if not db.get_username(params.getvalue("username")): 
        username_error = True
    if not db.get_email(params.getvalue("email")):
        mail_error = True
    if params.getvalue("pass1") != params.getvalue("pass2"): 
        password_error = True

    if not username_error and not mail_error and not password_error: 
        db.create_user(params.getvalue("username"), params.getvalue("email"), params.getvalue("pass1"))
        print("Location:login.py")


base.start_html()
print('''
<h2>Registracija korisnika</h2><br>
    Korisnicko ime: <input type="text" name="username" value="" placeholder="Upisite ime"><br><br>
    Email: <input type="text" name="email" value="" placeholder="Upisite svoju email adresu"><br><br>
    Lozinka: <input type="password" name="pass1"><br><br>
    Ponovite lozinku: <input type="password" name="pass2"><br><br>
    
    <input type="submit" value="Register">
       
''')

base.end_html()

if os.environ["REQUEST_METHOD"].upper() == 'POST':
    if username_error:
        print('<div>Zauzeto korisniko ime!Unesite novo ime.</div>')
    if mail_error:
        print('<div>Zauzet email!Unesite novi email.</div>')
    if password_error:
        print('<div>Lozinka i ponovljena lozinka nisu iste</div>')


