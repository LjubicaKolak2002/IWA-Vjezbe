#!C:\ProgramData\Anaconda3\python.exe

print('''
<!DOCTYPE html>
<html>
    <body>
        <h2>Forma 1</h2>
        <form action="test2.py" method="post">
        <table>
            <tr>
            <td>Ime:  </td>
            <td><input type="text" name="firstname" value="" placeholder="Upisite ime"></td>
            </tr>
          
            <tr>
            <td>Lozinka:   </td>
            <td><input type="password" name="pass1" value="" placeholder="Upisite lozinku"></td>
            </tr>

            <tr>
            <td>Ponovite lozinku:  </td>
            <td><input type="password" name="pass2" value="" placeholder="Upisite lozinku"></td>
            </tr>

            <tr>
            <td><input type = "submit" value="Next"></td>
            </tr>


        </form>
    </body>


</html>
''')