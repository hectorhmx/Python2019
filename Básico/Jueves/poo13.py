class Perro:
    """
    Cuando anteponemos dos guiones bajo a un atributo o un
    método, Python le agrega al nombre de dicho atributo
    o método un guión bajo y el nombre de la clase
    """
    __patas = 4  #  -> _Perro__patas
    pelaje = True

    def __init__(self, Nom, Raza):
        self.nombre = Nom
        self.raza = Raza
        print('Se ha creado un nuevo perro')

    def __comer(self, alimento):  # -> _Perro__comer
        print('Soy %s y estoy comiendo %s' % (self.nombre, alimento))

    def ladrar(self):
        print('WOOOFF!!')


perro1 = Perro('Rufus', 'Dálmata')
perro1.ladrar()
perro1._Perro__comer("pollo")
print(perro1._Perro__patas)

# El objetivo principal de esto es poder diferenciar métodos
# de clases que son heredados de los métodos de las clases
# que los heredan
