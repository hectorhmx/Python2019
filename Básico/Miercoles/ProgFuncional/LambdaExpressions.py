"""
5
Usando funciones Anonimas con Lambda
También llamadas funciones de una sola linea

Python Basico 2019-2

"""
#############################################################
def sumar(x,y):
	return x+y
b=(lambda x,y: x+y)(1,2)
#####################################################
def multiplicar(x):
    return 3*x + 1

g = lambda x: 3*x + 1
g(2)
#########################################################
lista = [2,5,6,12]
l1=[]
########################################################3
def cuadrados():
	for i in range(len(lista)):
		l1.append(lista[i]**2)
	print("Funcion sin usar lambda", l1)
cuadrados()

Cuad = list(map(lambda x:x**2, lista)); print("Funcion usando lambda", Cuad)
############################################################
def ec_cuadraticas(a,b,c):
    return lambda x: a*x**2 + b*x + c
    
g = lambda a,b,c,x: a*x**2 + b*x + c
############################################################
def es_par():
	for i in range(len(lista)):
		if lista[i]%2==0:
			print("Par")
		else:
			print("Impar")
print(es_par())

lamb = list(map(lambda n:n %2 ==0, lista))
print(lamb)
#############################################################

#Fibonacci con lambda
fib =(lambda n: n if n<2 else fib(n-1)+fib(n-2))

print(fib(10))

# filter() hace lo mismo que map solo que la funcion debe ser verdadera o falsa
# si es falsa, no añade el valor a la nueva lista

li2=filter(lambda n: n%2==0,lista)   # multiplos de 4
print("Los multiplos de la lista 1: ",list(li2))