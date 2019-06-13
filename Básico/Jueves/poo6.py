class Persona:

    def __init__(self, Nom):
        self.nombre = Nom
        self.estado = 'descansado'

    def correr(self):
        if self.estado == 'cansado':
            print('%s no puede! Está agotad@' % self.nombre)
        else:
            print('%s está haciendo ejercicio' % self.nombre)
            self.estado = 'cansado'

    def dormir(self):
        if self.estado == 'descansado':
            print('%s no puede! Tiene mucha energía' % self.nombre)
        else:
            print('ZZZ....')
            self.estado = 'descansado'


if __name__ == '__main__':
    persona1 = Persona('gali')
    persona2 = Persona('diego')

    print(persona1.estado)  # self = persona1
    print(persona2.estado)  # self = persona2

    persona2.correr()
    persona2.correr()
    persona2.dormir()
    print(persona2.estado)
