"""
goo.gl/YLr827
1
Funciones de Primer Clase y de orden Superior
Python Basico 2019-2
"""
def saludar(func):
	def saludar_es():
		print("Hola")

	def saludar_en():
		print("Hi")

	def saludar_fr():
		print("Bonjuor")

	def saludar_al():
		print("Hallo")

	###Diccionario que elige que funcion es la que se
	### Ejecuta
	dic_func = { "es" : saludar_es,
				"en" : saludar_en,
				"fr" : saludar_fr,
				"al" : saludar_al}
	return dic_func[func]
f=saludar("en")
f()


def calculadora(func):
	def suma(num1, num2):
		print(num1+num2)

	def resta(num1, num2):
		print(num1 - num2)

	def multi(num1, num2):
		print(num1 * num2)

	def div(num1, num2):
		print(num1/num2)
	
	dic_op= { "suma" : suma,
			"resta" : resta,
			"multiplicacion" : multi,
			"division" : div}

	return dic_op[func]
calculadora("multiplicacion")(40,3)
