
###############################################DICCIONARIOS###################################


#Un diccionario es una estructura de datos y un tipo de objeto en Python con características 
#especiales que nos permite almacenar cualquier tipo de valor como enteros, cadenas, listas,
#etcétera. Además, los diccionarios permiten identificar cada elemento mediante una clave (Key).

#Declaración de un diccionario: Se encierra el listado de valores entre llaves. Los pares clave/valor
#se separan mediante comas, mientras que la clave y el valor se separan con dos puntos.
diccionario = {'nombre':'Diego','apellido':'Casillas','edad':22,'cursos':['python','linux','java']}

#Podemos acceder a sus elementos mediante las claves que les correspondan

diccionario['nombre']
diccionario['apellido']
diccionario['cursos']

#Al ser posible insertar listas dentro de diccionarios, podemos acceder a sus índices.

diccionario['cursos'][0]

#También pueden recorrerse los diccionarios mediante la estructura for

for i in diccionario:
	print(i,":",diccionario[i])

#Función dict: Recibe como parámetro una representación de un diccionario y devuelve un 
#diccionario de datos.

diccionario = dict(nombre='Diego',apellido='Casillas')
diccionario

#Función zip: Recibe un par de elementos iterables con el mismo número de elementos.
#Devuelve un diccionario relacionando los elementos i-ésimos de cada elemento iterable
#usado como parámetro.

a = '1234'
b = ['uno','dos','tres','cuatro']

diccionario = dict(zip(a,b))

diccionario

#Método items: Devuelve una lista de tuplas, compuestas por dos elementos:
#El primer elemento es la clave y el segundo elemento es el valor que le corresponde.

diccionario
items = diccionario.items()

items

#El objeto que devuelve es de la clase dict_items, para poder hacer operaciones con él,
#podemos convertirlo a lista así:
items = list(items)

#Método keys: Devuelve una lista que contiene las llaves del diccionario.

diccionario =  {‘a’ : 1, ’b’ : 2, ‘c’ : 3 , ‘d’ : 4}
claves = diccionario.keys()
claves

#Método values: Devuelve una lista que contiene los valores del diccionario.

diccionario =  {‘a’ : 1, ’b’ : 2, ‘c’ : 3 , ‘d’ : 4}
valores = diccionario.values()
valores

#Método clear: Elimina los ítems del diccionario.

diccionario =  {‘a’ : 1, ’b’ : 2, ‘c’ : 3 , ‘d’ : 4}
diccionario.clean()
diccionario

#Método copy: Devuelve una copia del diccionario original.

diccionario =  {‘a’ : 1, ’b’ : 2, ‘c’ : 3 , ‘d’ : 4}
diccionario2 = diccionario.copy()
diccionario2

#Método fromkeys: Recibe como pŕámetros un iterable y un valor, devolviendo 
#un diccionario que contiene como claves los elementos del iterable con el 
#mismo valor ingresado.

diccionario = dict.fromkeys(['a','b','c','d'],1)
diccionario

#Método get: Recibe como parámetro una clave y devuelve el valor correspondiente.

diccionario
nuevo = diccionario.get('a')
nuevo

#Método pop: Recibe una clave, elimina esta y devuelve su valor.

diccionario
nuevo = diccionario.pop('a')
nuevo
diccionario

#Método setdefault: Puede funcionar de dos maneras: como get y para agregar nuevos 
#elementos.

#Como get
dic = {‘a’ : 1, ’b’ : 2, ‘c’ : 3 , ‘d’ : 4}
valor = dic.setdefault(‘a’)
valor

#Para añadir
dic = {'a':1, 'b':2, 'c':3 , 'd':4}
dic.setdefault('e',5)
dic

#Método update: Recibe como parámetro otro diccionario, si tienen claves iguales
#actualiza su valor, y si no hay claves iguales el par se añade al diccionario.

dic1 = {1:'dos',2:'dos'}
dic2 = {1:'uno',3:'tres'}

dic1.update(dic2)

dic1