'''
class Coche:
    def arrancar(self):
        print('RUUUMMM!!!')

coche1 = Coche()
coche1.color = 'naranja'

coche2 = Coche()
coche2.color = 'rojo'
'''


class Coche:
        """
        El método __init__ se le conoce como método constructor,
        este se manda a llamar cuando se crea una nueva instancia
        de la clase y sirve para realizar acciones cuando se crea
        un nuevo objeto y para asignarle atributos al mismo
        """
        # Son DOS guiones bajo, init, DOS guiones bajo
    def __init__(self, Col):
        self.color = Col
        '''
        cuando creemos a coche1 va a ser...
        coche1.color = Col
        cuando creemos a coche2 va a ser...
        coche2.color = Col
        '''
        print('Se creó un nuevo coche')

    def arrancar(self):
        print('RUUUMMMMM!!!')


coche1 = Coche('naranja')  # self = coche1 y Col = 'naranja'
coche2 = Coche('rojo')  # self = coche2 y Col = 'rojo'
print(coche2.color)

# self va a adquirir el valor de la instancia
