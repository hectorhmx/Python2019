# CSV -> Comma Separated Values
# Es el formato mas usado para importar y exportar datos de hojas de caluclo y bases de datos

# Podemos crear uno en google sheets

import csv

with open('calificaciones.csv') as archivoLect:
	lectura = csv.reader(archivoLect)
	# podemos iterar sobre lectura y obtendremos
	# listas de los elementos de cada fila
	for listaFila in lectura:
		print(listaFila)

# Podemos utilizar otros delimitadores diferentes de ','
with open('calificaciones2.csv') as archivoLect:
	lectura = csv.reader(archivoLect, delimiter=':')
	for listaFila in lectura:
		print(listaFila)

califNueva = ['Enrique',7,7,7]

with open('calificaciones.csv') as archL, open('califNuevas.csv','w') as archE:
	lectura = csv.reader(archL)
	escritura = csv.writer(archE, delimiter='!')
	for listaFila in lectura:
		escritura.writerow(listaFila)
	escritura.writerow(califNueva)