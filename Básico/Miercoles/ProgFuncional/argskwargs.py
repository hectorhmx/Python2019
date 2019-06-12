# Podemos especificar que un parámetros
# va a recibir múltiples valores poniendo
# un * antes de su nombre
##Estos llegarán a modo de tupla
def func(a,*c):
	print(a)
	print(c)

#func(2,4,1,2,5,7,"hola")

# Por lo general, a esta variable se le 
# nombra args
def func2(a,*args):
	print(a)
	print(args)


# Podemos especificar un parámetro que
# va a recibir los argumentos por llave
# que sobren, se nombran kwargs por
# convención y se colocan dos * antes de su
# nombre
def func4(a,b,**kwargs):
	print(a)
	print(b)
	print(kwargs)

#func4(2,4,p=2,h=3,g=20)


###¿Como mezclar todas?
##Ordenen = normales, default, args, kwargs
def func5(a,b,c="hola",*args,**kwargs):
    print(a,b)
    print(args)
    print(kwargs)
    print(c)
func5(1,2,"bai","help","tengo sueño",miAmor="No existe",tarea="demasiada")
##Primero los posicionales, luego los kword
##c= bai
