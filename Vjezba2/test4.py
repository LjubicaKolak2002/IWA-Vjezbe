#!C:\ProgramData\Anaconda3\python.exe

import cgi
data = cgi.FieldStorage()

print('')
print('<html>')
print('<body>')
print('<h2>Uneseni podaci</h2>')
print('<br>')
print('Ime: ', data.getvalue("ime"))
print('<br>')
print('Email: ', data.getvalue("email"))
print('<br>')
print('Status: ', data.getvalue("status"))
print('<br>')
print('Smjer: ', data.getvalue("smjer"))
print('<br>')

if data.getvalue("zavrsni"):
  print("Zavrsni: ", data.getvalue("zavrsni"))
else:
  print("Zavrsni: Ne")

print('<br>')

if data.getvalue("napomene"):
  print("Napomene: ", data.getvalue("napomene"))
else:
  print("Napomene: Nema napomena")

print('<br>')
print('<a href="test1.py">Na pocetak</a>')
print('</body>')
print('</html>')


