#4
def principal(f): ##F es el nombre de la funcion que le pasamos como aprametros
	def nueva():
		print("iniciando", f.__name__) ##es un metodo magico para saber el nombre de nuestra funcion
		f() ###ejecutar lo que hace nuestra funcion
		print("Finalizando", f.__name__)

@principal
def decorada():
	print("Funcion Decorada")



def decorador_args(arg1, arg2, arg3):
	def wrap(f):
		print("Inicializando Funcion Wrap")
		def wrapped_f(*args):
			print("iniciando wrapped_f")
			print("Argumentos del Decorador: ", arg1, arg2, arg3)
			f(*args)
			print("Fin wrapped_f")
		return wrapped_f
	return wrap

@decorador_args(1,2,3)
def fun(a,b, c):
	print("Argumentos de la funcion: ",a, b, c)

p=fun("a1", "a2", "a3")
print(p)
