class NumeroComplejo:
    ParteReal = 0
    ParteImaginaria = 0
    ##Metodos de la clase
    ##Constructor de la clase
    def __init__ (self, real, imaginaria):
        self.ParteReal = real
        self.ParteImaginaria = imaginaria
    ##imprimir imaginaria
    def imprimirNumero(self):
        print(str(self.ParteReal)) + "+ "+ str(self.ParteImaginaria) + 'i')
