class Terrestre:
    def respirar(self):
        print('Respiro fuera del agua')

    def caminar(self):
        print('Estoy caminando')


class Acuatico:
    def respirar(self):
        print('Respiro bajo del agua')

    def nadar(self):
        print('Estoy nadando')

# Herencia múltiple


class Anfibio(Acuatico, Terrestre):
    # Dependiendo del orden en el que coloquemos
    # las clases de las que hereda, dependerá
    # cuál método respirar heredará
    def saludar(self):
        print('Hola, soy un anfibio')


if __name__ == '__main__':
    rana = Anfibio()
    rana.caminar()
    rana.nadar()
    rana.respirar()

    pez = Acuatico()
    pez.respirar()

# Notese que pez y rana realizan la acción respirar
# sin embargo, en cada caso, el resultado es diferente,
# a esta carácterística se le denomina polimorfismo, en
# el que el comportamiento de un método va a depender de
# que objeto lo esté realizando.
