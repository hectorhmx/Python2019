import sqlite3

con = sqlite3.connect('Base1.db')
cursor = con.cursor()

def crear_tabla():
	cursor.execute('''
		CREATE TABLE SEMESTRE(
		    SEMESTRE_ID     NUMBER(18, 0)    NOT NULL PRIMARY KEY,
		    ANIO            NUMBER(4, 0)     NOT NULL,
		    PERIODO         NUMBER(1, 0)     NOT NULL,
		    FECHA_INICIO    DATE             NOT NULL,
		    FECHA_FIN       DATE             NOT NULL
		)
		''')
	cursor.execute('''
		CREATE TABLE estudiante(
			estudiante_id NUMBER(10) NOT NULL,
			nombre VARCHAR2(90) NOT NULL,
			direccion VARCHAR2(90) NOT NULL,
			calificacion NUMBER(10),
			grado_actual VARCHAR2(90) NOT NULL
	
			)
		'''
		)
	cursor.execute("INSERT INTO estudiante VALUES(1, 'Dafne Cabrera Garibaldi', 'Su casa', 10, '4to primaria')")
	cursor.execute("INSERT INTO estudiante VALUES(2, 'Berenice Medel Sanchez', 'Su casa', 12, '8vo Semestre')")
	cursor.execute("INSERT INTO estudiante VALUES(3, 'Jorge Luis Chavez Delgado', 'Su casa', 9, '10 Semestre')")
	cursor.execute("INSERT INTO estudiante VALUES(4, 'Andrea Garcia Ruiz', 'Su casa', 9, '6to Semestre')")

def insertar_tabla():
	tabla_nombre = input("en que tabla desea insertar? ")
	datos = input("Que datos desea insertar? ")
	cadena ="INSERT INTO "+ tabla_nombre+ " VALUES (" + datos+")"
	cursor.execute(cadena)
	con.commit()

def eliminar_tabla():
	t=int(input("Desea eliminar:\n1.-Tabla\n2.-Dato de una tabla"))
	if t ==1:
		tabla_nombre = input("De que tabla desea eliminar: ")	
		cadena = "DELETE FROM "+ tabla_nombre 
		cursor.execute(cadena)
		con.commit()
	
	if t ==2:
		try:
			tabla_nombre = input("De que tabla desea eliminar: ")
			ids= (input("Cual es el id del dato que desea borrar: "))
			cadena = "DELETE FROM "+ tabla_nombre+' WHERE '+tabla_nombre+'_id = '+ids
			cursor.execute(cadena)
			con.commit()	
		except Exception as e:
			con.commit()
			print("Ocurrio un error",e)

def actualizar_tabla():

	instruc_nom = input("De que tabla desea actualizar?: ")
	instruc_datoo = input("Que dato desea Actualizar: ")
	instruc_nuevo = input("A que dato desea actualizar: ")
	cadena ="UPDATE "+instruc_nom+"SET "+instruc_datoo+" ="+instruc_nuevo
	cursor.execute(cadena)
	con.commit()

def ver():
	instruc = input("De que tabla desea obtener valores?\n>>")
	cadena = "SELECT * FROM " + instruc
	for row in cursor.execute(cadena):
		print(row)
	con.commit()

while True:
	try:
		crear_tabla()
		while True:
			op= int(input("Que desea hacer?\n1.-Insertar\t2.-Eliminar\t3.-Actualizar\t4.-Ver valores\t5.-Salir\t6.-Insertar comando sql\n>>"))
			if op ==1:
				insertar_tabla()
			if op ==2:
				eliminar_tabla()
			if op==3:
				actualizar_tabla()
			if op==4:
				ver()
			if op==5:
				break
			if op==6:
				comand=input("SQL>")
				cursor.execute(comand)
	except:
		print("Ocurrio un error La base se crerrar")
		con.close()
		break

#crear_tabla()