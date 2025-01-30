#!C:\ProgramData\Anaconda3\python.exe

import cgi
data = cgi.FieldStorage()

if data.getvalue("pass1") != data.getvalue("pass2") or data.getvalue("pass1") == None:
  print("Location:test1.py")

print('''
<!DOCTYPE html>
<html>
    <body>
        <h2>Forma 2</h2>
        <form action="test3.py" method="post">
            <table> 
            <tr>
            <td>Status: </td>
            <td><input type="radio" name="status_studenta" value="Redovan">Redovan
            <input type="radio" name="status_studenta" value="Izvanredan">Izvanredan</td>
            </tr>
          

            <tr>
            <td>Email: </td>
            <td><input type="email" name="mail" value="" placeholder="Upisite vas email"></td>
            </tr>

            <tr>
            <td>Smjer: </td>
            <td><select name="smjer_studija">
              <option value="Racunalne mreze">Racunalne mreze</option>
              <option value="Programiranje">Programiranje</option>
              <option value="Informacijski sustavi">Informacijski sustavi</option>
              <option value="Baze podataka">Baze podataka</option>
            </td>

           <tr>
           <td>Zavrsni: </td>
           <td><input type="checkbox" name="zavrsni_rad" value="Da">Da</td>
           </tr>

           <tr>
           <td><input type = "submit" value="Next"></td>
           </tr>

        </table>
''')

print ('<input type="hidden" name="ime" value="' + data.getvalue("firstname") + '">')

print('''
        </form>
    </body>


</html>
''')

print('<br>')
print('Ime: ', data.getvalue("firstname"))
