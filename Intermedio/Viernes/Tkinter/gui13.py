# CHECKBUTTON
from tkinter import *

# Cuando usamos Checkbuttons generalmente queremos
# que el usuario pueda escoger cero, uno o más de estos
# por este motivo debemos saber el estado de cacda uno de
# ellos, ya sea activo o inactivo, por esto a cada uno de
# ellos se les asocia una variable

raiz = Tk()
variables = [] #Inicializamos una lista vacia

var1 = IntVar()
chk1 = Checkbutton(raiz, text='Primer', variable=var1) #Le asociamos la variable var1 al chk1
chk1.pack()
variables.append(var1) #Agregamos a la lista el valor del primer Checkbutton

var2 = IntVar()  # Variable de tipo int
chk2 = Checkbutton(raiz, text='Segundo', variable=var2) #Le asociamos la variable var2 al chk2
chk2.pack()
variables.append(var2)#Agregamos a la lista el valor del segundo Checkbutton

"""
entradas = ['Primero', 'Segundo', 'Tercero', 'Cuarto', 'Quinto']

for entrada in entradas:
    var = IntVar()
    Checkbutton(raiz, text=entrada, variable=var).pack()
    variables.append(var)
"""


def darEstados():
    for variable in variables:
        print(variable.get(), end=' ') #Imprime en consola lo que hay en ese momento en la lista 'variable'
    print() #Salto de linea


Button(raiz, text='Estados', command=darEstados).pack()

raiz.mainloop()
