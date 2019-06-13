###########################
# POO
# Métodos mágicos
###########################

#Metodos que se mandan a llamar cuando para cierta cosa, modificamos con ellos los objetos

class Coordenada:

	def __init__(self,x,y):
		self.x=x
		self.y=y

	# Se manda a llmar cuando se quiere sumar los objetos por medio del operador +
	def __add__(self, otro):
		return  Coordenada(self.x+otro.x,self.y+otro.y)

	#__sub__(-)#__mul__(*)#__div__(/)#__pow__(**)#__mod__(%)
	
	#Se manda llamar cuando se manda a imprimir el objeto por medio de print
	def __str__(self):
		return "(%d,%d)"%(self.x,self.y)

	#Se manda llamar cuando se requiere acceder al objeto como si fuera una lista[]
	def __getitem__(self, indice):
		if indice==0:
			return self.x
		else:
			return self.y

	def __setitem__(self, indice, valor):
		if indice==0:
			self.x = valor
		else:
			self.y = valor

c1 = Coordenada(45,20) #Se manda a llamar a __init__
c2 = Coordenada(15,30) #""
print (c1) #llamado a __str__()
print (c1+c2) #llamando a __add__
c1[0] = 89 #se manda a lamr a __setitem__
print(c1[0])# se manda a llamar __getitem