# Ejercicio BUTTON Y LABEL
#Boton de aumentar y disminuir un número
from tkinter import *

contador = 0
def funcA(): #funcion aumentar
	global contador #Se puede acceder a la variable global dentro o fuera de la función.
	contador += 1
	label.config(text = contador) #cambiamos el texto de la etiqueta al llamar a esta función

def funcD(): #funcion disminuir
	global contador
	contador -= 1
	label.config(text = contador) 


raiz = Tk()
raiz.title('Contador') #Cambia titulo de la ventana

label = Label(raiz, text = contador, bg = 'blue')
boton1 = Button(raiz, text = 'aumentar', command = funcA)
boton2 = Button(raiz, text = 'disminuir', command = funcD)

label.pack(fill = BOTH, expand = YES, side = TOP)
boton1.pack(fill = BOTH, expand = YES, side = RIGHT)
boton2.pack(fill = BOTH, expand = YES, side = LEFT)
raiz.mainloop()