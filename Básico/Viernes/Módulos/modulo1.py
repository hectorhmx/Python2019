########### Métodos de importación##########
"""
1.-
import modulo

modulo.fun(parámetros)
"""
import math #impotamos math
x = math.sin(2) #math.sin(2) me devuelve el seno de cualquier número, en este caso de 2
print('\tEl seno de 2 es:', x) # imprimimos el resultado guardado en la variable x
sin = '\tNo tengo nada, pero me llamo como una función trigonométrica' 
print(sin)
# Puedo tener variables en mi código con el mismo nombre que las que importo, como 'sin', que es una cadena de texto.

"""
2.-
import modulo as m
m.fun(parámetros)
"""
import math as m # importamos math con un alias/apodo. Cada que necesitemos una función de math la mandaremos llamar con m.nombreDeLaFunción.
y = m.degrees(m.pi) # 'degrees'convierte un ángulo en radianes  a grados
# pi radianes es 180 grdos, es lo que nos mostrará en pantalla si lo imprimimos
print('\n\n\tEl valor de ', m.pi, 'radianes en grados es: ', y)

"""
3.-
from modulo2 import pot, a
pot(3, 3)
print(a)
"""
from time import sleep # importamos el módulo time, el cual contiene una función llamada 'sleep'. Esta función sleep detiene la ejecución del programa
print('\n\n\tVoy a poner atención a clase.')
sleep(10) # con sleep, el programa espera la cantidad de segundos especificados entre paréntesis
print('\tNo me dormí, estaba parpadeando lento')

"""
4.-
from modulo2 import *
pot(3, 3)
print(a)
print(b)
"""
from random import * # del módulo random importamos todo. Esta es una mala práctica, pues se utilizan recursos innecesariamente, pero sirve para comprender el tema de importar módulos.
z = randint(-2,2) #randint permite arrojar un número aleatorio entre los dos  parámetros que recibe.
print('\n\n\tUn número aleatorio entre -2 y 2 es: ' ,z)

"""Ejercicio Importa el módulo math, y utilizando las entidades sin y pi, calcúla:
  cos(1/π) y sin(π/2)"""

import math
x = math.cos(1/math.pi)+math.sin(math.pi/2)
""" Ejercicio 2: Calcula el área de un círculo (de radio 2 unidades, r=2) de dos maneras:
1.- De manera manual creando tus variables.
2.- Importando el módulo math, y utilizando la entidad pi.

Pista, puedes utilizar 
este valor para pi.
pi = 3.1416
area=pi*radio**2
"""
import math
radio = 2
pi = 3.1416
areamanual = pi*radio**2
areamath = math.pi*radio**2
print('\n\n\tEl área del círculo obtenida de manera manual es:', areamanual)
print('\tEl área del círculo obtenida con el módulo math es:', areamath)


