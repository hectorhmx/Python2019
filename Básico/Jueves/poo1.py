"""
Para crear una nueva clase debemos usar la palabra reservada class
seguido del nombre de la clase y dos puntos
"""


class Animal:
    """
    Los métodos de la clase se declaran al igual que las funciones, solo
    que estos deben encontrarse dentro del bloque de código de la clase
    y deben tener como primer parámetro 'self'
    """

    def alimentarse(self):  # Método alimentarse
        print('Me estoy alimentando!!')

    def respirar(self):  # Método crecer
        print('Estoy respirando!!!')


animal1 = Animal()  # Creamos dos instancias de la clase Animal
animal2 = Animal()  # Nombre de la clase seguido de dos paréntesis


if __name__ == '__main__':
    # Mandamos a llamar el método alimentarse de animal1
    # Notese que no es necesario poner ningún argumento aunque en la
    # definición pusimos como parámetro a self
    animal1.alimentarse()
    animal2.respirar()
