from poo1 import Animal

"""
class Animal:

    def alimentarse(self):  # Método alimentarse
        print('Me estoy alimentando!!')

    def respirar(self):  # Método crecer
        print('Estoy respirando!!!')
"""


class Pato(Animal):
    def cuackear(self):
        print('CUACKKK!!!!!')

    '''
    def alimentarse(self): # Redefinimos el método de la clase Pato
        print('Como granos de maiz')
    '''


pato1 = Pato()
pato1.cuackear()
pato1.respirar()
