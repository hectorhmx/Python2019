
class Perrito():
    general = {"patas":4,"ojos":2,"orejas":2}
    def __init__(self,nombre,color):
        self.color = color
        self.nombre = nombre
    def bark(self):
        print("woff woff")
    def sing(self):
        print("Perritos malvados, perritos encarcelados")

mamut = Perrito("Mamuth","cafe")
jett = Perrito("Jett","blanco")

lista = [mamut,jett]*5
##ver que tiene sla lista
print(lista)

###Si queremos ver que todo esta bien, podemos debuggear

###no funciono :c y menos en programas muy grandes y complicados
for perrito in lista:
    perrito.bark()
for perrito in lista:
    perrito.sing()

