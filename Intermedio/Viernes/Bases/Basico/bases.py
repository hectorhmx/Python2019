import sqlite3

def base_paises():
	con = sqlite3.connect('paises.db')
	cursor = con.cursor()
	##Creando tablas
	cursor.execute('''
		CREATE TABLE paises(
			pais_id NUMBER(10) PRIMARY KEY,
			nombre VARCHAR2(20),
			continente VARCHAR(20),
			lengua VARCHAR2(90),
			moneda VARCHAR2(15)
			)
		''')
	cursor.execute('''
		CREATE TABLE estudiante(
			estudiante_id NUMBER(10) CONSTRAINT estudiante_id_pk PRIMARY KEY,
			nombre VARCHAR2(90) NOT NULL,
			direccion VARCHAR2(90) NOT NULL,
			calificacion NUMBER(10),
			grado_actual VARCHAR2(90) NOT NULL
	
			)
		'''
		)
	##insertando valores en las tablas
	cursor.execute("INSERT INTO paises VALUES(1, 'Mexico', 'Americano', 'Espanol', 'Peso Mexicano')")
	cursor.execute("INSERT INTO paises VALUES(2, 'China', 'Asiatico', 'Chino', 'Peso Chino')")
	cursor.execute("INSERT INTO paises VALUES(3, 'Inglaterra', 'Europa', 'Inles', 'Libra Esterlina')")
	cursor.execute("INSERT INTO paises VALUES(4, 'Egipto', 'Africano', 'Egipcio', 'Peso Egipcio')")
	##Valores a la tabla estudiante
	cursor.execute("INSERT INTO estudiante VALUES(1, 'Dafne Cabrera Garibaldi', 'Su casa', 10, '4to primaria')")
	cursor.execute("INSERT INTO estudiante VALUES(2, 'Berenice Medel Sanchez', 'Su casa', 12, '8vo Semestre')")
	cursor.execute("INSERT INTO estudiante VALUES(3, 'Jorge Luis Chavez Delgado', 'Su casa', 9, '10 Semestre')")
	cursor.execute("INSERT INTO estudiante VALUES(4, 'Andrea Garcia Ruiz', 'Su casa', 9, '6to Semestre')")
	##Guardando los valores con la sentencia commit
	con.commit()
	print("Valores en la tabla paises")
	for row in cursor.execute('SELECT * FROM paises'):
		print(row)
	print("Valores en la tabla estudiante")
	for row in cursor.execute('SELECT * FROM estudiante'):
		print(row)
	##Eliminar Tablas
	cursor.execute("DELETE FROM estudiante")
	con.commit()
	con.close()
base_paises()	