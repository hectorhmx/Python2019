#Programa para contar las palabras de un archivo de texto y editarlo al final, escribiendo al último
#el número de palabras con las que cuenta
#De no especificar el modo, por default se abren en modo de lectura,
#Por lo cual, la línea de abajo podía ser escrita así:
#archivo = open('prueba.txt')
archivo = open('prueba.txt', 'r')

###La manera  de imprimir un archivo en python es: 
for linea in archivo:
	print(linea)

archivo.seek(0) #Para regresar el puntero a la posición inicial
#Ahora, hay que contar las palabras.
listaArchivo = archivo.readlines() 
contadorPalabras = 0
#El método readlines convierte cada línea del archivo en una lista 
print(listaArchivo)
for elemento in listaArchivo:
	#Se le suma al contador de palabras la longitud de las listas de cada línea
	contadorPalabras += len(elemento.split())



print("El archivo tiene ", contadorPalabras, 'palabras')