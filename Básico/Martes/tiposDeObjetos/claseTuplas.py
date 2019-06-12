
##########################TUPLAS#######################################

#La declaración de una tupla es muy parecida a la de una lista, sin embargo, se usan paréntesis
#en lugar de corchetes:

miTupla = ("hola",("t","o"),2)

#Al igual que con las listas, podemos usar la notación del operador ":"

miTupla[:]
miTupla[:1]
miTupla[1:]
miTupla[1:2]

#Como lo mencionamos, una tupla es inmutable:

miTupla[0] = 200 # Esta línea va a generar un error

#Usamos la función len para conocer el número de elementos contenidos en la tupla

len(miTupla)

#Pueden existir tuplas vacías, de cero componentes

t0 = ()
len(t0)

#También pueden existir tuplas unitarias, pero tienen un pequeño detalle.
#Python exige que la componente no sólo se encierre entre paréntesis, también se 
#le debe poner una coma a continuación del valor de la componente.

t1 = (80)
type(t1)

t1 = (80,)
type(t1)

#Si a una variable se le asigna una secuencia de valores separados por comas, el valor de
#esa variable será la tupla formada por todos los valores asignados. Esta operación se 
#conoce como empaquetado de tuplas.

a = "esto"
b = "es"
c = "una"
d = "tupla?"

tupla = a,b,c,d
tupla
type(tupla)

#Si se tiene una tupla de longitud k, se puede asignar la tupla k a variables distintas y en 
#cada variable quedará una de las componentes de la tupla. A esta operación se le denomina 
#desempaquetado de tuplas.

tupla = ("estas","son","variables","independientes")
a,b,c,d = tupla

a
b
c
d