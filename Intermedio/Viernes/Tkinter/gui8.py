# Aplicación de FRAME

from tkinter import *

raiz = Tk()
frame1 = Frame(raiz, bg='#7FE82C', height=50, width=20)
frame2 = Frame(raiz, bg='#0D88FF', height=50, width=20)
# Podemos especificar los colores de esta forma
#height y width indican el tamaño del frame


frame1.pack(side=LEFT, fill=BOTH, expand=YES)
frame2.pack(side=RIGHT, fill=BOTH, expand=YES)


btn1 = Button(frame1, text='boton 1')
# frame1 es el widget padre de btn1
btn1.pack(side = TOP)

btn2 = Button(frame1, text='boton 2')
btn2.pack(side = BOTTOM)

'''

def noHacerNada():
    return None

#protocol refers to the interaction between the application and the window manager.
raiz.protocol('WM_DELETE_WINDOW', noHacerNada)  # lambda:None
# alteramos el protocolo que se genera al apretar el boton X para cerrar
# la ventana, y hacemos que al ser apretado no haga nada
Button(frame1, text='Saludar', relief=FLAT, command=(lambda: print('Hola'))).pack(side=TOP)
Button(frame1, text='Salir', command=raiz.quit).pack(side=BOTTOM)
# El método quit termina el mainloop, por lo tanto, termina con la interfaz
# Éste método lo poseen la mayoría de los widgets, como Button, Label y Frame

Label(frame2, text='Botones').pack(side=LEFT, anchor=E)
# anchor permite especificar posición con respecto a puntos cardinales
# N, NE, NW, S, etc.
'''
raiz.mainloop()