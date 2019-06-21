import shelve

# shelve nos permite guardar objetos serializados con pickle
# en un formato similar al de los diccionarios

db = shelve.open('baseDatos')
# shelve.open crea un archivo o lo abre en caso de ya existir
# este archivo tiene una extención db (data base). Se puede 
# decir que shelve almacena los datos en una base de datos

# Se almacena de igual forma que los elementos de un diccionario
# Es necesario que las llaves sean de tipo string
db['telefonos'] = {'Victoria':5538490092, 'Aldo':5528394827}
db['numeros'] = [1,2,3.2,4+5j]
db['dias'] = ('Lu','Ma','Mi','Ju','Vi','Sa','Do')

db.close()

with shelve.open('baseDatos') as db:
	db['palabra'] = 'hola Mundo'