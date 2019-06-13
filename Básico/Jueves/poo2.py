# Por convención, las clases empiezan con letra mayúscula


class Coche:
    def arrancar(self):
        print('RUUUMMMMM!!')


coche1 = Coche()
coche2 = Coche()

coche1.arrancar()

print(coche1 == coche2)
# Son de la misma clase pero son objetos diferentes

coche2.color = 'rojo'
# Podemos crear y asignar atributos conforme a la marcha

print(coche2.color)
