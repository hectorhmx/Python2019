import shelve

with shelve.open('baseDatos') as db:

	# Podemos ver cuantos elementos hay con la función len
	print(len(db))

	print(list(db.items()))

	# Podemos crear una lista de llaves 
	print(list(db.keys()))

	# Podemos crear una lista de elementos
	print(list(db.values()))


	# Podemos acceder a los elemenos de la misma forma que
	# lo haríamos con diccionarios
	print(db['telefonos'])
	print(db['dias'])
	db.pop('numeros')
	#print(db['numeros'])
	print(list(db.items()))