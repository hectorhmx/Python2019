# JSON es un formato nuevo para el intercambio de datos
# Java Script Object Notation
# Está diseñado para ser neutral entre los lenguajes de programación

import json
from pprint import pprint as print
#The pprint module provides a capability to “pretty-print” arbitrary Python data structures in a form which can be used as input to the interpreter. 

nombre = dict(nombre = 'Juanito', apellidos = ['Pérez','Prado'])
# diccionario = {'nombre': 'Luis Alberto', 'apellidos': ['Garrido','Mendoza']}

datos = dict(nombres = nombre, trabajo = ['policía','cartero','taquero'], edad = 23)
print(datos)

with open('archivoJSON.json', 'w') as archE:
	#json.dumps(datos)
	json.dump(datos, fp = archE, indent = 3)
	#Un objeto de python puede ser convertido a un string JSON con .dump()
	# Creamos un nuevo archivo con los datos
	# almacenados en formato json

with open('archivoJSON.json') as archL:
	datosCargados = json.load(archL)
	# nos retorna un diccionario con los datos

print(type(datosCargados))
print(datosCargados['trabajo'])
