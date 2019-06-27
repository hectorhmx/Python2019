# ENTRY
#Entrada de texto
from tkinter import *

raiz = Tk()

ent = Entry(raiz)  # entrada de texto
boton = Button(raiz, text='Mandar')

# Variables de tkinter

var = StringVar()  # variable de tipo string
ent.config(textvariable=var)  # asociamos variable con ent

'''
Variables de control

Las variables de control son objetos especiales que se asocian a los widgets para almacenar sus valores y 
facilitar su disponibilidad en otras partes del programa. Pueden ser de tipo numérico, de cadena y booleano. '''


def mandar():
    print('Recibido: ', var.get())  # var.get nos regresa un string con
    # lo que esté escrito en la entrada de texto
    var.set('') 


boton.config(command=mandar)


ent.pack(side=LEFT, expand=YES, fill=X)
boton.pack(side=RIGHT)
raiz.mainloop()
