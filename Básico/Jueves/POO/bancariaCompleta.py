####Ejemplo completo de clases

#####incio de la clase
class CuentaBancaria:
	##Variables de clase
	saldo = None  
	nombre = None
	##metodo constructor
	def __init__(self, saldo, nombre):
		###Revisamos si las varibales de entrada son del tipo especifico
		if type(saldo) == int or type((saldo) == float) and isinstance(nombre, str):
			self.saldo = saldo
			self.nombre = nombre
			self.mostrarInformacion()
		else:
			self.saldo = 0
			self.nombre = "Desconocido"
			self.mostrarInformacion()

	def mostrarInformacion(self):
		print(self.nombre + "Cuenta con: " + str(self.saldo) + "de saldo")

	def deposito(self, cantidad):
		if type(cantidad) == int or type(cantidad) == float:
			print("Deposito de " +self.nombre + "por: " +str(cantidad))
			####incrementar la cantidad de saldo
			self._calcularSaldo(cantidad + self.saldo) #### Comprobar
			self.mostrarInformacion()
		else:
			print("Deposito de  "+ self.nombre+ "por: " + str(cantidad))
			print("Las cantidades deben ser numeros")

	def retiro(self, cantidad):
		if type(cantidad) == int or type(cantidad) == float:
			print("Retiro de "+self.nombre+ "por: "+str(cantidad))
			cantidadRetirar = cantidad
			if cantidadRetirar > self.saldo:
				print(self.nombre+ "No hay saldo suficiente")
			else:
				##Reducir la cantidad de saldo de la cuenta
				self._calcularSaldo(self.saldo - cantidadRetirar)
				self.mostrarInformacion()
		else:
			print("retiro de "+self.nombre+"por: "+str(cantidad))
			print("las cantidades deben de ser numeros")

	def _calcularSaldo(self, cantidad):
		##obtener el saldo asociado a la cuenta
		self.saldo = cantidad

###Creacion objetos
objeto1 = CuentaBancaria(12, "Luvi")
objeto2 = CuentaBancaria(125, "Dubi  Dooo!")
######manipualcion de objetos
objeto2.retiro(89)
objeto1.retiro(12000)
##objeto1.deposito("Mil Docientos")
