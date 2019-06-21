import sqlite3
con = sqlite3.connect('Bases.db')
cursor = con.cursor()

carga = open('Carga.sql','r') ##abrimos nuestro archivo en modo lectura

for i in carga:
    print(i)
    cursor.execute(i)

#linea = carga.readline()
#print(linea)
#cursor.execute('''INSERT INTO estudiante VALUES(10000, 'Dafne Cabrera Garibaldi', 'Su casa', 10, '4to primaria')''')
con.commit()
for row in cursor.execute('SELECT * FROM pelicula'):
    print(row)
con.close()
carga.close()