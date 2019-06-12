##Ya hemos trabajado con funciones anteriormente 
print("Hola mundo")
##Estas funciones se llaman Built Ins, vienen junto con python

## Podemos definir nuestras propias funciones
###Definicion, puede estar en cualquier parte, pero siempre antes de usarla
def diHola():
    print("Hola")
##LLamar a la funcion
#diHola()

##Ejemplo de Built ins:
#list() Convertir a lista
#abs()
#max()
#len()
#isinstance()
#hasattr()


##De este modo, podemos encapsular codigo, y retuilizarlo
##Principio  DRY, Dont repeat yourself. Ejemplo:
def ponerMusica():
    print("Abre youtube")
    print("Poner nombre de la cancion")
    print("Listo")

##¿Si queremos decir lo que esta dentro 3 veces?
#podemos copiar y pegar, o:
ponerMusica()
print("hare mis tareas")
ponerMusica()
print("Me ire a bañar")
ponerMusica()

##Pero ahora quiero modificarlo porque ya tengo spotify
##cambiar print(Youtube) a print("Spotify")


# Las funciones pueden retornar valores
# Se hace con la palabra reservada return
def funcion2():
	a = 3
	b = 2
	return a+b

r = funcion2()
print(r)
# Cuando una función llega a un return, termina

def funcion3():
	a = "hola"
	b = "que"
	c = "hace"
	return a+b+c
	print('Adios')

r = funcion3()
print(r)

def funcion1():
	a = 3
	b = 2
	print(a+b)
    
# Una función que no tiene un return
# por default retorna None

r = funcion1()
print(r)

# Puede haber múltiples return en una
# función, pero el primero que alcance 
# va a ser el usado

def func():
	if 3 > 4:
		return "tres es mayor"
	else:
		return "tres es menor"

r = func()
print(r)

##Seguir con parametros.