#!C:\ProgramData\Anaconda3\python.exe

import cgi
data = cgi.FieldStorage()

print('''
<!DOCTYPE html>
<html>
    <body>
        <h2>Forma 3</h2>
        <form action="test4.py" method="post">
            <table>

            <tr>
            <td>Napomene:</td>
            <td><textarea name="napomene" rows="3" placeholder="Upisite eventualne napomene"></textarea>
            </tr>
        
            <tr>
            <td><input type = "submit" value="Next"></td>
            </tr>

          </table>
''')

print ('<input type="hidden" name="ime" value="' + data.getvalue("ime") + '">')
print ('<input type="hidden" name="email" value="' + data.getvalue("mail") + '">')
print ('<input type="hidden" name="status" value="' + data.getvalue("status_studenta") + '">')
print ('<input type="hidden" name="smjer" value="' + data.getvalue("smjer_studija") + '">')
print ('<input type="hidden" name="zavrsni_rad" value="' + data.getvalue("zavrsni") + '">')

print('''
        </form>
    </body>


</html>
''')
