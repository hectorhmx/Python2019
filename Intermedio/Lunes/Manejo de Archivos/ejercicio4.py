print('Bienvenido a la Agenda persistente, ¿qué acción quieres realizar?')
def menu():
	print('1.- Agregar contacto\n2.- Modificar contacto\n3.- Ver Lista de Contactos\n4.- Eliminar contactos\n5.- Salir')
menu()
eleccion = '0'
while eleccion != '5':
	#eleccion = input('Bienvenido a la Agenda persistente, ¿qué acción quieres realizar?')
	eleccion=input()
	if eleccion == '1':
		with open('agenda.txt','a') as agenda:
			datos =['\nnombre',' ','numero\n']
			datos[0] = input('Nombre del contacto: ')
			numero = input('Número telefónico: ')
			datos[2] = numero+'\n'
			agenda.writelines(datos)
			menu()
	elif eleccion == '2':
		#El signo '+' permite realizar ambas operaciones. La diferencia entre w+ y r+ 
		#consiste en que la primera opción borra el contenido anterior antes de escribir nuevos datos, 
		#y crea el archivo en caso de ser inexistente. a+ se comporta de manera similar, 
		#aunque añade los datos al final del archivo.
		modificado=input("¿A quién deseas modificar?\n")
		nuevoNombre = input("Ingresa su nuevo nombre: ")
		nuevoNumero = input("Ingresa su nuevo numero: ")
		agenda = open('agenda.txt','r')
		listasAuxiliares = agenda.readlines()#Convierte en listas el archivo
		agenda.close()
		#SE abrió el archivo a propósito para borrar todo y solamente cambiar la linea necesaria
		agenda = open('agenda.txt','w')
		for linea in listasAuxiliares:
			#La variable auxiliar a, almacena la linea de texto convertida en lista
			#Cada elemento de dicha lista, corresponde a una palabra
			a = linea.split() 
			if a[0] == modificado:
				agenda.write(nuevoNombre+' '+nuevoNumero+'\n')
			else:
				agenda.write(linea)
		agenda.close()
		menu()
	elif eleccion == '3':
		print('Tus contactos son:\n')
		with open('agenda.txt','r') as agenda:
			for i in agenda:
				print(i)
		menu()
	elif eleccion == '4':
		eliminado=input("¿A quién deseas eliminar?\n")
		agenda = open('agenda.txt','r')
		listasAuxiliares = agenda.readlines()#Convierte en listas el archivo
		agenda.close()
		#SE abrió el archivo a propósito para borrar todo y solamente cambiar la linea necesaria
		agenda = open('agenda.txt','w')
		for linea in listasAuxiliares:
			a = linea.split()
			if a[0] == eliminado:
				pass
			else:
				agenda.write(linea)
		agenda.close()
		menu()