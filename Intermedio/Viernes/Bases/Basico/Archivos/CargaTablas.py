import sqlite3 ### Importamos la libreria SQLITE3
con = sqlite3.connect('Bases.db') ##Creamos nuestra conexion a bases
cursor = con.cursor() 

creacion = open('Definicion.sql','r') ###Abrimos nuestro archivo en modo lectura
l = creacion.readlines() ##Leeemos todo nuestro archivo en modo lectura
###Esto nos va a devolver las cadenas en formato lista

#print(l)
#print(type(l))
cadena = "" ## DEfinimos una cadena vacia
for i in l: ##Recorremos nuestra lista elemento por elemento
	if i == ";\n": ##Si encontramos el separador ";" entonces 
		cadena.replace('\n', ' ') ###Le quitamos los saltos de linea
		cadena.replace(';', '') ##Y reemplazamos los puntos y comas por cadenas vacias
		cursor.execute(cadena) ##Ejecutamos nuestra cadena 
		cadena = "" ##Vaciamos la cadena
		#print(cadena) ##
		input("Cadena vacia") ##Aclaramos que la cadena esta vacia
		con.commit() ##Guardamos nuestros cambios en la base
	else: ##Si no ha encontrado los ";", entonces recorremos hasta encontrar saltos de linea
		cadena = cadena + i ##Y solo los cambiamos por espacios en blanco
		cadena.replace('\n', ' ')
		print(cadena)

if len(cadena) > 1: ##Si el rango de la cadena es mayor a 1, entonces ejecutamos lo ultimo que contenga
	input("La cadena aun contiene algo: ")
	print(cadena)
	cursor.execute(cadena)
	con.commit() ##Guardamos nuestros cambios
#cursor.execute(cadena)
#con.commit()
con.close()
creacion.close()