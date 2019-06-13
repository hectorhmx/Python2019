"""
La encapsulacion se refiere a la delimitación del acceso a determinados metodos y atributos
de los objetos en una clase. Esto permite crear una interfaz segura entre el usuario
y el codigo
"""
class NumeroComplejo:
    ParteReal = 0
    ParteImaginaria = 0
    ##Metodos de la clase
    ##Constructor de la clase
    def __init__ (self, real, imaginaria):
        self.ParteReal = real
        self.ParteImaginaria = imaginaria

    ##imprimir numero
    def imprimirNumero(self):
        print(str(self.ParteReal) + "+ "+ str(self.ParteImaginaria) + 'i')
    
    ##Cambiar parte Real (setter)
    def cambiarParteReal(self, real):
        self.ParteReal = real
    
    ##Obtener Parte real (getter)
    def obtenerParteReal(self):
        return self.ParteReal
    
    ##Cambiar parte Imaginaria (setter)
    def cambiarParteImaginaria(self, imaginaria):
        self.ParteImaginaria =  imaginaria
    
    ##Obtener parte imaginaria (getter)
    def obtenerParteImaginaria(self):
        return self.ParteImaginaria
primerNumero = NumeroComplejo(12,4)
print("Version 1 del numero")
primerNumero.imprimirNumero()
print("Modificando el numero")
primerNumero.cambiarParteImaginaria(90)
primerNumero.cambiarParteReal(56)
primerNumero.imprimirNumero()
print("Utilizando getter y setters")
print("Usando Getter para obtener y cambiar la aprte imaginaria")
print(primerNumero.obtenerParteImaginaria()+8)
