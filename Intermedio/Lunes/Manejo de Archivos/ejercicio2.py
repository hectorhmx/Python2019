#En este programa, vamos a contar las líneas de un archivo sin siquiera verlo.
#Comenzamos abriendo el archivo, que en mi caso, se llama poema.txt
archivo  = open('poema.txt','r')
lineas = 0
for i in archivo:
	if i == "\n":
		pass
	else:
		lineas+=1
archivo.close()

print('El documento tiene ',lineas, ' renglones para leer.')