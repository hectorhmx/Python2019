"""
Se debe crear una clase Empleado, los empleados van a contar con un salario de
horas normales y con un salario de horas extra. Las primeras 48 horas de trabajo
son consideradas como horas normales, y por lo tanto, se pagan con el salario
de horas normales, después de esto, las horas van a ser consideradas como horas
extra y por lo tanto van a ser pagadas con el salario de horas extra. Los
trabajadores van a poder trabajar un determinado número de horas y van a poder
cobrar.
"""


class Empleado:
    def __init__(self, NOMBRE,  SUELDOHN, SUELDOHE):
        self.nombre = NOMBRE
        self.sueldoHN = SUELDOHN
        self.sueldoHE = SUELDOHE
        self.horas = 0

    def trabajar(self, HORAS):
        print('%s está trabajando' % self.nombre)
        self.horas += HORAS

    def consultarPaga(self):
        if self.horas <= 48:
            return self.horas * self.sueldoHN
        else:
            return 48 * self.sueldoHN + (self.horas - 48) * self.sueldoHE

    def cobrar(self):
        print('%s acaba de recibir %s' % (self.nombre, self.consultarPaga()))
        self.horas = 0


if __name__ == '__main__':
    empleado1 = Empleado("Jorge", 400, 500)
    empleado2 = Empleado("Ana", 500, 600)

    empleado1.trabajar(10)
    print(empleado1.consultarPaga())
    empleado1.cobrar()
    print(empleado1.consultarPaga())

    empleado2.trabajar(48)
    print(empleado2.consultarPaga())
    empleado2.trabajar(1)
    print(empleado2.consultarPaga())
