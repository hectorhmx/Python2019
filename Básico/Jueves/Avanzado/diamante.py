###problema del diamante
###en el casod e python, soluciona el problema del diamante lo implementa:
### en codigo de abajo hacia arriba
### en forma esquematica de iquierda a derecha
class A:
	def a(self):
		print("A")

class B(A):
	def b(self):
		print("B")

class C(A):
	def c(self):
		print("C")

class D(C, B):
	def pregutaporA(self):
		self.a()

ObjetoD =D()
ObjetoD.pregutaporA()
print(D.__mro__)