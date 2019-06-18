class Padre:
    def __init__ (self):
        print("Constructor clase padre")
    def metodo(self):
        print("Ejecutando metodo de clase padre")

###Si el metodo constructor de la clase hija no se declara, esta tomara
### automaticamente el metodo constructor de la clase padre
class Hija(Padre):
    def met_hija(self):
        print("Metodo de la clase Hija ")

h = Hija()
h.metodo()
h.met_hija()