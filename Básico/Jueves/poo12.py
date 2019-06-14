class Coche:
    llantas = 4  # Atributos de la clase Coche
    numeroCoches = 0

    def __init__(self, Color, Marca="Ferrari"):
        self.color = Color  # atributos de instancias de la clase coche
        self.marca = Marca
        Coche.numeroCoches += 1


if __name__ == '__main__':
    coche1 = Coche('rojo')
    coche2 = Coche('amarillo', 'Bocho')
    print(coche1.llantas)
    print(Coche.llantas)
    Coche.llantas = 3
    print('Nuevo num de llantas...')
    print(coche2.llantas)
    print(coche1.numeroCoches)
    print(Coche.numeroCoches)
