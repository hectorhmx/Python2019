class Perro:

    def __init__(self, Nom, Raza):
        self.nombre = Nom
        self.raza = Raza

    def comer(self, alimento):
        print('Soy %s y estoy comiendo %s' % (self.nombre, alimento))

    def ladrar(self):
        print('WOOOFF!!')


if __name__ == '__main__':
    perro1 = Perro('Luna', 'Border Collie')
    perro2 = Perro('Maya', 'Labrador')

    # Tienen la misma característica (nombre) con diferentes valores
    print(perro1.nombre)  # self = perro1
    print(perro2.nombre)  # self = perro2
    print(perro1.raza)

    # Realizan la misma acción de formas diferentes
    perro2.comer('Pavo')  # self = perro2
    perro1.comer('Dog Chow')  # self = perro1
    perro1.ladrar()
