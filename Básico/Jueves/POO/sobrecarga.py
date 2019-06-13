###Sobrecarga de opreadores usando metodos magicos
###Metodos Magicos
class Vector:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, v):
        # Sumar dos Vectores
        return Vector(self.x + v.x, self.y + v.y)

    def __sub__(self, v):
        # Restar dos Vectores
        return Vector(self.x - v.x, self.y - v.y)

    def __mul__(self, s):
        # Multiplicar un Vectores por un escalar
        return Vector(self.x * s, self.y * s)

    def __div__(self, s):
        # Dividir un vector por un escalar
        float_s = float(s)
        return Vector(self.x / float_s, self.y / float_s)

    def __floordiv__(self, s):
        # Parte entera de la divicion de un vector sobre un escalar
        return Vector(self.x // s, self.y // s)

    def __repr__(self):
        # Imprima una representación amistosa de la clase Vector. De lo contrario, sería
        # <__main__.Vector instance at 0x01DDDDC8>.
        return '<Vector (%f, %f)>' % (self.x, self.y, )


a = Vector(3, 5)
b = Vector(2, 7)
print(a + b)   # Output: <Vector (5.000000, 12.000000)>
print(b - a)   # Output: <Vector (-1.000000, 2.000000)>
print(b * 1.3) # Output: <Vector (2.600000, 9.100000)>
print(a // 17) # Output: <Vector (0.000000, 0.000000)>
print(a / 17) 