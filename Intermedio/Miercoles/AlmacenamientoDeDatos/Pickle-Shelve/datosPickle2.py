import pickle

with open('datos.pkl', 'rb') as archivoL:
	listaObtenida = pickle.load(archivoL)
	# pickle.load nos permite desserializar el objeto
	# que se contenía en el archivo
	print(listaObtenida)
	print(listaObtenida[2])