class Operacion: ##Inicio de la clase Padre Operacion
    ##Atributos de la clase
    valor1 = 0
    valor2 = 0
    ##Metodos de la Clase
    ##Constructor de la clase
    def __init__(self, numero1, numero2):
        self.valor1 = numero1
        self.valor2 = numero2
    
    ##Obtener Valor 1 (getter)
    def obtenerValor1(self):
        print(self.valor1)
        return self.valor1

    
    ##Obtener Valor 2 (getter)
    def obtenerValor2(self):
        print(self.valor2)
        return self.valor2
    
    ##Cambiar valor1(setter)
    def cambiarValor1(self, nuevoValor):
        self.valor1 = nuevoValor

    ##Cambiar valor2(setter)
    def cambiarValor2(self, nuevoValor):
        self.valor2 = nuevoValor

    ##imprimir Valor
    def imprimirValor(self, numero):
        print(numero)
#################Utilizando la clase orignal#########################
numeros = Operacion(3,4)
print("El tipo de dato de una clase es: " + str(type(numeros)))
numeros.obtenerValor1() ##Obtener el valor del primer numero
numeros.imprimirValor(numeros.obtenerValor2())
numeros.cambiarValor1(90) ##Cambiando el valor 1
numeros.obtenerValor1()

###############################################
##Inicio de la clase Hija llamada Suma
class Suma(Operacion):
    ##Se llama al metodo constructor de la clase padre
    def __init__ (self, numero1, numero2):
        super().__init__(numero1, numero2)

    def sumar(self):
        self.imprimirValor(self.valor1 + self.valor2)

suma1 = Suma(10, 5)
print("Con el objeto suma")
suma1.obtenerValor1()
suma1.obtenerValor2()
suma1.sumar()
