
#####################LISTAS###############################

#Para crear una lista en Python, la sintaxis es la siguiente:
lista = [10,15,20,30]
#La lista anterior, está conformada por 4 elementos, pero una lista puede tener
#un número cualquiera de elementos.
#Podemos acceder a los elementos de la lista individualmente.
"""
El primer elemento de la lista, es el elemento 0, el segundo elemento
es el número 1, y así sucesivamente. Por ejemplo, si queremos acceder
al tercer elemento de "lista", lo hacemos así:
"""
lista[2]
#También podemos asignar valores de la lista a otra variable:
elemento3 = lista[2] # Se le asigna el tercer elemento de la lista a la nueva variable "elemento3"
elemento3 #Imprime la variable "elemento3", que es 20.
#Podemos acceder al último elemento de la lista mediante el índice -1
#Podemos acceder al penúltimo elemento de la lista mediante el índice -2
#Podemos acceder al antepenúltimo elemento de la lista mediante el índice -3
#Y así sucesivamente...
lista[-1]
lista[-2]
lista[-3]
lista[-4]

#¿Qué tipo de variable retorna la consola cuando escibimos "elemento3 == lista[2]"
#¿Qué valor tiene?
#Regresa un Booleano, True

#Una lista puede contener datos de distintos tipos, e incluso anidar otras listas:

lista2 = [1,1.0,"1",[1,[1,2,3]],(1,5,6),True] 

#Para saber la longitud de una lista, usamos la función len()

len(lista2)

#Además, las listas son mutables, es decir, pueden modificarse.

lista2[-1] = False #Modifica el último elemento de lista2
lista2[0] = 2 #Modifica el primer elemento de lista2
lista2 #Imprime lista2, ya modificada

#Para recorrer una lista con facilidad, podemos usar un ciclo for:
for i in lista2:
    print(i)

#Podemos dividir la lista con el operador ":":
#Si se elimina el primer número, los elementos comenzaran desde el principio. 
#Si se elimina el segundo número, los elementos irán al final.

lista2[2:4] #Devuelve una lista del tercer al cuarto elemento
lista2[:5]  #Devuelve una lista del primer al quinto elemento
lista2[1:]  #Devuelve una lista del segundo al último elemento
lista2[:]   #Devuelve una lista idéntica a lista2

#Se puede cambiar la lista bajo la misma lógica:

lista2[2:5] = ["Cambié","la lista",";D"]

#Método insert: Sirve para insertar un elemento en la lista, recibe dos argumentos:
#El primer argumento es el índice de la posición donde queremos insertar el nuevo elemento.
#El segundo argumento es el objeto que queremos insertar.

lista3 = [1,3,4,5]
lista3.insert(1,2)
lista3

#Método append: Sirve para agregar un elemento al final de la lista.
#Recibe un solo argumento: el objeto a añadir.

lista3.append(6)
lista3

#Método extend: Sirve para añadir más de un elemento al final de una lista.
#Recibe un argumento: la lista que contiene los elementos a añadir.

listaParaCompletar = [7,8,9]
lista3.extend(listaParaCompletar)
lista3

#Método sort: Sirve para ordenar una lista. Si es una lista numérica, por default la ordena
#de menor a mayor. Si es una lista de Strings, la ordena alfabéticamente.

listaDesordenada = [1,5,6,3,2]
listaDesordenada.sort()

listaDesordenada = ["Xóchitl","Sonia","Any","Malala","Juancho"]
listaDesordenada.sort()

#Si queremos ordenar las listas en sentido contrario (de mayor a menor o inverso al 
#orden alfabético), el método sort() recibe como parámetro reverse=True.

listaDesordenada = [1,5,6,3,2]
listaDesordenada.sort(reverse=True)

listaDesordenada = ["Xóchitl","Sonia","Any","Malala","Juan"]
listaDesordenada.sort(reverse=True)

#Método index: Recibe como argumento el elemento de una lista y retorna el índice que le
#corresponde.

lista = ["índice 0","índice 1","índice 2"]
lista.index("índice 1")

#Método pop: Puede recibir uno o ningún parámetro. Recibe el índice del elemento a eliminar.
#Si no se especifica el índice, eliminará el último elemento

lista = ["no","te","quiero",",para nada"]
lista.pop()
lista
lista.pop(0)
lista

#Método remove: Sirve para eliminar elementos de una lista al especificar el elemento.

lista = [1,2,3,4,6784,5,"achisAchisLosMariachis"]
lista.remove(6784)
lista

#Funciones útiles:

lista = [1,2,3,4,5]
min(lista) #retorna el valor mínimo en la lista
max(lista) #retorna el valor máximo en la lista
sum(lista) #retorna la suma de los valores de la lista

#También se puede eliminar un elemento mediante el operador del

del lista[-1]
lista

#Comparación de Listas

lista1 = [1,2,3,4,5]
lista2 = [1,2,3,4,5]

lista1 == lista2

lista2.pop()

lista1 == lista2

#Operaciones con listas

#Las listas pueden sumarse:
lista1+lista2

#También pueden multiplicarse
lista1*5

#Método split: Sirve para separar cadenas y convertirlas en lista, recibe como parámetro
#el caracter que queremos usar para dividir la cadena.

cadena = "Soy una frase convertida en lista"
cadena = cadena.split()
cadena

cadena = "Estoy.delimitada.por.puntos"
cadena = cadena.split(".")
cadena

#Método reverse: Sirve para invertir el orden de una lista en Python

a = "redrum" #Declara una cadena de nombre "a"
a=list(a) #Convierte "a" en lista
a #Imprime "a", ya como lista
a.reverse() #Invierte el orden de los elementos en "a"
a #Imprime la lista "a", ahora invertida

#Método join: Sirve para unir una lista y convertirla en cadena.
#El método se aplica a un delimitador (string) y recibe como parámetro la lista a unir.

a
delimitador = ""
cadena = delimitador.join(a)
cadena

delimitador = "OwO"
cadena = delimitador.join(a)
cadena

#Método copy: Crea una copia superficial de una lista, para evitar aliasing al mutarla

a = [1,2,3,4,5]
b = a

b.pop()
a #b es otro nombre para el mismo objeto, por eso la lista a fue afectada al 
#aplicarle el método pop a la lista b.

a = [1,2,3,4,5]
b = a.copy()

b.pop()
a #Esta vez, la lista a no se modificó porque la lista b es una copia de a, no sólo otro nombre.
