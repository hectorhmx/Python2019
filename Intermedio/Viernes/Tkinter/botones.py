from tkinter import *
ventana = Tk()
ventana.title('usando Botones')
boton1 = Button(ventana,text="Boton NORMAL")
boton1.grid(row=1,column=1)
boton2 = Button(ventana,text="Boton FLAT",relief=FLAT) ###Plano
boton2.grid(row=1,column=2)
boton3 = Button(ventana,text="Boton SUNKEN",relief=SUNKEN) ###Hundido
boton3.grid(row=1,column=3)
boton4 = Button(ventana,text="Boton RIDGE",relief=RIDGE)
boton4.grid(row=1,column=4)
boton5 = Button(ventana,text="Boton SOLID",relief=SOLID) ###Solidos
boton5.grid(row=1,column=5)
ventana.mainloop()