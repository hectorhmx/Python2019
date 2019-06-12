
##################CONJUNTOS#########################

#Para crear un conjunto, se especifican sus elementos
#entre llaves. 
#En un conjunto no podemos incluir objetos mutables, 
#como listas, diccionarios u otros conjuntos.

s = {True,2,2,2,3.78,"Hola",None,(1,2,3),5}

#Al tratarse de un conjunto, aunque hayamos ingresado
#tres veces el número 2, en el conjunto únicamente se 
#encuentra una vez.

s
#la línea anterior debería devolver:
#    {True, 2, 3.78, 'Hola', 5, (1, 2, 3), None}

#Para crear un conjunto vacío, se debe hacer una
#instancia de la clase set, de lo contrario,
#python interpretará que queremos crear un diccionario
#vacío.

conj = {}
type(conj)

conj = set()
conj
type(conj)

#Podemos crear un conjunto mediante cualquier objeto
#iterable.

lista1 = [1,2,3,4]
conjunto1 = set(lista1)
conjunto1

conjunto2 = set(range(10))

#Un set puede ser convertido a list

lista2 = list(conjunto2)
lista2
type(lista2)

#También, una list puede ser convertida en set

lista = [1,2,2,3,3,4]
conjunto = set(lista)
conjunto
type(conjunto)

#Métodos add y discard: Sirven para añadir y remover
#elementos de un conjunto.

conj = {1,2,3,9,5}
conj.add(4)
conj
conj.discard(9)
conj

#Función clear: Elimina todos los elementos

conj.clear()
conj

#Método pop: Retorna un elemento de la función

conj.pop()
conj.pop()

#Como en matemáticas, los conjuntos pueden ser operados:

#Unión: se realiza con el caracter | y retorna un 
#conjunto que contiene los elementos que se encuentran 
#en al menos uno de los dos conjuntos involucrados.

a = {1,2,3}
b = {3,4,5}
a | b

#Intersección: se realiza con el caracter & y retorna
#un conjunto con los elementos que se encuentran en
#los conjuntos involucrados.

c = {"tres",3,6}
a & b & c

#Diferencia: La diferencia de a menos b, retorna un
#conjunto con los elementos de a que no están en b.

a = {1,2,3,4}
b = {2,3}
a-b

#Principio de extensionalidad:  Dos conjuntos son 
#iguales si y solo si contienen los mismos elementos.

{1,2,3} == {3,2,1}

#El conjunto B es un subconjunto de A cuando todos
#los elementos de B pertenecen también a A.
#Podemos determinar esto con python mediante el 
#método issubset().

a = {1,2,3,4,5}
b = {2,4}
c = {6,9}
b.issubset(a)
c.issubset(a)

#De manera inversa, decimos que A es un superconjunto
#de B.

a.issuperset(b)
a.issuperset(c)

#############TODO CONJUNTO ES SUBCONJUNTO#############
##################Y SUPERCONJUNTO DE##################
#######################SÍ MISMO#######################

#La diferencia simétrica entre dos conjuntos, nos 
#retorna un conjunto que contiene los elementos que 
#pertenecen a sólo alguno de los conjuntos involucrados.
#Retorna un nuevo conjunto que contiene
#los elementos que pertenecen a alguno de los dos
#conjuntos que participan en la operación, pero no a
#ambos

a = {1,2,3,4}
b = {3,4,5,6}

a.symmetric_difference(b)

#Conjuntos disconexos: Un elemento es disconexo 
#respecto de otro si no comparten elementos entre
#sí.

a = {1,2,3}
b = {3,4,5}
c = {5,7,8}

a.isdisjoint(b)
a.isdisjoint(c)

#Conjuntos inmutables: La diferencia entre un conjunto
# y un conjunto inmutable, es análoga a la diferencia
#entre una lista y una tupla.
#Ambas comparten todas las operaciones de conjuntos, 
#excepto las que implican alterar sus elementos, como 
#add o discard.

a = frozenset({1,2,3})
a.add(3)
b = {4,5,3}
a | b