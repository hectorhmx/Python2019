"""
3
Python Basico 2019_2

La función Map nos permite aplicar una operación sobre cada uno de los items de una lista.
El primer argumento es la función que vamos a aplicar y el segundo argumento es la lista.
"""
import math

lista = [1, 34, 56, 45, 34]
l1 = []
########################################3
##Funcion que suma
def sumar(sum1):
	return sum1 + 10
##Sin map
def sinmap():
	for i in lista:
		l1.append(i+10)
	print("Funcion sin map: ", l1)
#sinmap()

##Conmap
#resultado = list(map(sumar, lista))
#print("Usando map ", resultado)


###########Sim     map##############################
potencias=[2,3,4]
def Cuadrados():
	for i in range(len(potencias)):
		l1.append(pow(lista[i],potencias[i]))
	print("Funcion sin map", l1)
#Cuadrados()
##Con Map
#resultado = list(map(pow, lista, potencias))
#print("Funcion con map",resultado)


#########################################
def Seno():
	for i in range(len(lista)):
		l1.append(math.sin(lista[i]))
	print("Funcion sin map", l1)
#Seno()

##Con map
#resultado = list(map(math.sin, lista))
#print("Funcion con map",resultado)

#########################################
def Coseno():
	for i in range(len(lista)):
		l1.append(math.cos(lista[i]))
	print("Funcion sin map", l1)
#Coseno()

###Con Map
#resultado = list(map(math.cos, lista))
#print("Funcion con map",resultado)


#########################################
def factorial():
	for i in range(len(lista)):
		l1.append(math.factorial(lista[i]))
	print("Funcion sin map", l1)
factorial()

###Con Map
resultado = list(map(math.factorial, lista))
print("Funcion con map",resultado)
############################################

############################################