# BUTTON

from tkinter import *
from webbrowser import open_new #Módulo Para abrir páginas web

# Función que se va a ejecutar cuando se
# presione el botón 1

def fun1(): # LAS FUNCIONES NO RECIBEN PARÁMETROS
    print('Hola Mundo!!')

# Función que se va a ejecutar cuando se
# presione el botón 2

def fun2():
    print('Bye a todos!!!')


def buscarGoogle(): 
    open_new("https://www.google.com")
    

raiz = Tk()
raiz.title('Dos Botones') # Titulo a la ventana
raiz.geometry('200x100') # Nos permite definir tamaño inicial de ventana

label = Label(raiz, text='Tres botones que hacen algo') #Command hace que podamos enviarle una función al evento del click sobre el botón
boton1 = Button(raiz, text='Saludar', command=fun1, bd=12)
boton2 = Button(raiz, text='Despedir', command=fun2)
boton3 = Button(raiz, text = "GOOGLE", command = buscarGoogle, bg = "red")

label.pack(side=TOP)
boton1.pack(side=LEFT, fill=BOTH, expand=YES)
boton2.pack(side=RIGHT, fill=BOTH, expand=YES)
boton3.pack(side = TOP)
# Colocamos todo en la ventana raiz

raiz.mainloop()
