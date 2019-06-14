from poo12 import Coche


class CocheN(Coche):

    # Para poder llamar un método de una clase sin necesidad
    # de crear o utilizar una instancia de la misma, la tenemos
    # que declarar como un método estático, esto se logra colocando
    # un decorador encima de l método que queramos
    @staticmethod
    def darNumCoches():
        # Los métodos estáticos no tienen como primer parámetro self
        print('Hay %s coches' % CocheN.numeroCoches)


CocheN.darNumCoches()  # No es necesario crear un coche para
# poder llamar un método estático de la clase
coche1 = CocheN("rojo")
coche2 = CocheN("amarillo")
coche1.darNumCoches()
