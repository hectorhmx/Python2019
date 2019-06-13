from poo5 import Perro


class Chihuahua(Perro):
    def __init__(self, Nom):
        # Realizamos el mismo constructor de la clase Perro,
        # perro ponemos como raza a "Chihuahua"
        Perro.__init__(self, Nom, "Chihuahua")

    def ladrar(self):  #  Redefinimos el método ladrar
        print('wif..!')


if __name__ == '__main__':
    chi1 = Chihuahua('Rico')
    chi1.ladrar()
    chi1.comer("croquetitas")
    print(chi1.raza)
    print(chi1.nombre)
