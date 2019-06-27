# Ejercicio ENTRY

from tkinter import *
from random import choice #Choice nos permite elegir aleatoriamente un objeto perteneciente a una lista, tupla o string

raiz = Tk()
label = Label(raiz, text = "Hola a todos!!")
entrada = Entry(raiz) 							#Objeto de entrada de texto
btnCambiarColor = Button(raiz, text = 'Cambiar color')
btnCambiarText = Button(raiz, text = 'Cambiar texto')

var = StringVar()
entrada.config(textvariable = var)

colores = ['red','blue','green','yellow','purple']

def cambiarColor():
    label.config(bg = choice(colores)	)

def cambiarTexto():
    label.config(text = var.get())
    var.set('') #metodo para cambiar el valor de la variable de control var (Es tipo StringVar())

btnCambiarColor.config(command = cambiarColor) #Asignamos las funciones a los botones
btnCambiarText.config(command = cambiarTexto)

label.pack()
entrada.pack()
btnCambiarColor.pack()
btnCambiarText.pack()
raiz.mainloop()