"""
2
¿Funciones puras o Puras funciones?
Python Basico 2019_2
"""

def hola():
	print("Hola")

def factorial(n):
	fact = 1
	for i in range(1,n+1): 
		fact = fact * i 
	print("Factorial es:", fact)

##factorial(34)

def func_pure(a,b):
    x = a * b
    return x / (a + b)

def area_triang(h,b):
	a = (b*h)/2
	return a
#############################################3Recursividad
def factorial(x):
    if x == 1:
        return 1
    else:
        return x * factorial(x-1)
    
print(factorial(6))

###############################################################
def fiboRecursivo(n):
	if n==0:
		return 0
	elif n==1:
		return 1
	return(fiboRecursivo(n-1)+fiboRecursivo(n-2))

print("El fibonacci de %d es %d"%(0,fiboRecursivo(0)))
print("El fibonacci de %d es %d"%(1,fiboRecursivo(1)))
print("El fibonacci de %d es %d"%(2,fiboRecursivo(2)))
print("El fibonacci de %d es %d"%(3,fiboRecursivo(3)))
print("El fibonacci de %d es %d"%(10,fiboRecursivo(10)))
print("El fibonacci de %d es %d"%(100,fiboRecursivo(100)))



#####################################
##Help -> Turtle Demo -> tree, forest -> start