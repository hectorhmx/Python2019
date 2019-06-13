class Coche:
    def arrancar(self):
        print('RUUUUMMMM!!!')


coche1 = Coche()
coche2 = Coche()

coche1.arrancar()  # self = coche1

# Por qué no..
# coche2.arrancar(coche2)  # Especificamos el valor de self
# Python hace esto de manera automática
# Lo podríamos hacer de la siguiente forma
# Coche.arrancar(coche2)  # Esto es como hacerlo de forma manual..

# Coche.arrancar(coche2) => coche2.arrancar()
