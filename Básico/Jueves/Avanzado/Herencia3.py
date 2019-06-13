class Vehiculo:
    def __init__(self, marca, modelo, n_ruedas, velocidad):
        self.marca = marca
        self.modelo = modelo
        self.n_ruedas = n_ruedas
        self.velocidad = velocidad
    def acelerar(self):
        print("La velocidad actual es: " + str(self.velocidad*3) + " Km/hr")
    def frenar (self):
        print("La velocidad ACtual es: "+ str(self.velocidad*0.5) + " Km/hr")
class Moto(Vehiculo):
    pass

class Coche(Vehiculo):
    pass

class Bicicleta(Vehiculo):
    pass

c = Coche("BMW", "Shido", 4, 90)
c.acelerar()
c.frenar()