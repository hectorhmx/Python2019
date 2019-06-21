import sqlite3
con = sqlite3.connect('Bases.db')
cursor = con.cursor()

creacion = open('Definicion.sql','r')
l = creacion.readlines()

print(l)
print(type(l))
cadena = ""
for i in l:
	if i == ";\n":
		cadena.replace('\n', ' ')
		cadena.replace(';', '')
		cursor.execute(cadena)
		cadena = ""
		print(cadena)
		input("Cadena vacia")
		con.commit()
	else:
		cadena = cadena + i
		cadena.replace('\n', ' ')
		print(cadena)

if len(cadena) > 1:
	input("La cadena aun contiene algo: ")
	print(cadena)
	cursor.execute(cadena)
	con.commit()
#cursor.execute(cadena)
#con.commit()
con.close()
creacion.close()