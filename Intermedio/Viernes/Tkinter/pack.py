############################################
#Método PACK
###########################################

#Importamos el modulo
from tkinter import *

ventana=Tk()

Button(ventana,text="Arriba").pack(side=TOP,fill=Y,expand=YES)
Button(ventana,text="Centro").pack(side=TOP,fill=Y,expand=YES)
Button(ventana,text="Abajo").pack(side=TOP,fill=Y,expand=YES)

Button(ventana,text="Izquierda").pack(side=LEFT,expand=YES)
Button(ventana,text="Centrado").pack(side=LEFT,expand=YES)
Button(ventana,text="Derecha").pack(side=LEFT,expand=YES)



#Para mantener la ventana abierta
ventana.mainloop()
