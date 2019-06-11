"""
2
Python Basico 2019-2
Desde un punto de vista muy básico, un generador es un método para
extraer los resultados de una función de una forma diferente
a lo que tenemos acostumbrado a usar.

"""
import itertools

def gen():
	yield "Este"
	yield "Es "
	yield "un "
	yield "Generador"

a = gen()

print(type(a))
print(a)
###i=0
###print(a[i])

print(a.__next__())###Accedemos al sigueinte valor a traves de un metodo
##########################################################################################
def func_suma(a):
	fin = a + 10
	while  a < fin:
		a+=1
		yield a#,fin

for a in func_suma(1):
	print(a)
################################################################################
def multiplos_de(n):
    index = 0
    while index <=10:
        yield index*n
        index = index + 1

for i in multiplos_de(2):
	print(i)
