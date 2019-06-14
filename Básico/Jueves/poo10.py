class Perro:

    def __init__(self, Nom, Raza):
        self.nombre = Nom
        self.raza = Raza

    def comer(self, alimento):
        print('Soy %s y estoy comiendo %s' % (self.nombre, alimento))

    def ladrar(self):
        print('WOOOFF!!')

    # Cuando sumemos dos objetos de la clase Perro se va a
    # ejecutar el siguiente método
    def __add__(self, otroPerro):
        # print('Los perros se sumaron')
        # return Perro(Nombre, Raza)
        return Perro(self.nombre+' Jr', self.raza+'-'+otroPerro.raza)
        # Se va a retornar un nuevo objeto Perro


perro1 = Perro('Nala', 'Dalmata')
perro2 = Perro('Rex', 'Boxer')


perroHijo = perro1 + perro2
print(perroHijo.nombre)
print(perroHijo.raza)
perroHijo.ladrar()
