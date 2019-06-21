# Serialización de objetos:
# Convertir objetos en cadenas de bytes y viceversa
# Nos permite mantener objetos entre ejecuciones de 
# script y otro

# Serialización con pickle

import pickle

lista = [1,True, 3+4j, [1,2,3], {'a':3,'b':2}]

with open('datos.pkl', 'wb') as archivoE: # wb -> write bytes
	# pickle.dump(objeto, archivo)
	pickle.dump(lista, archivoE)
	# Serializa el objeto y lo guarda en el archivo