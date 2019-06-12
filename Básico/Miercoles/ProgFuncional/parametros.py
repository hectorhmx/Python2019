# Las funciones pueden recibir parámetros, estos
# van a definir las acciones o resultados que se 
# van a obtener

# ejemplo de Python

absoluto = abs(-4)
# identificar partes con preguntas
# retorna el absoluto de un número
# recibe como argumento un número
print(absoluto)

def miabs(num):
	if num < 0:
		return num*(-1)
	else:
		return num

absoluto = miabs(-4)

# en la función anterior, num es un parámetro
# y -4 es un argumento
print(absoluto)

# Las funciones pueden recibir muchos argumentos

def funcion(a,b,c):
	return a + (b*c)

print(funcion(2,5,3))
print(funcion(3,4,1))
#print(funcion(5,3))

# A este tipo de parámetros se les conoce como 
# parámetros posicionales, debido a que dependiendo
# del orden en el que coloquemos los argumentos, 
# definirá a que parámetro van a ser asignados

# Existe otro tipo de argumentos conocidos como 'keyword arguments'
# o argumentos por llave, con estos definimos a que parámetro se le
# debe asignar un argumento

r = funcion(b=3,c=4,a=2)
print(r)

# Que pasaría si queremos combinar?
# Inducir al error
# Es importante que si vamos a combinar posicionales con argumentos por 
# llave, se debe colocar los posicionales antes.

r = funcion(2,c=4,b=3)
print(r)

# funcion(c=4,b=3,2)

# ejemplo en Python en intérprete
# print -> Parámetros por default

# Con las funciones se pueden definir con argumentos por default,
# que en caso de no ser ingresados por el usuario, van a tener
# un valor predeterminado

def funcionNew(nom1, nom2, nom3 = 'Luis'):
	nombres = [nom1,nom2,nom3]
	for nombre in nombres:
		print('Hola',nombre)

funcionNew('Ana','Jorge','Andrea')
funcionNew('Ana','Jorge')

# Los argumentos por default deben colocarse después de los 
# posicionales

"""def funcion(nom1 = 'Ana', nom2, nom3):
	nombres = [nom1,nom2,nom3]
	for nombre in nombres:
		print('Hola',nombre)
"""

##Seguir con args y kwargs