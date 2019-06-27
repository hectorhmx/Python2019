from tkinter import *

master = Tk()

Label(master, text="First").grid(row=0)
Label(master, text="Second").grid(row=1)

e1 = Entry(master)
e2 = Entry(master)

e1.grid(row=0, column=1)
e2.grid(row=1, column=1)


Button(master,text="Boton").grid(row=2,columnspan=2,sticky=S+N)
Button(master,text="Boton").grid(row=2,column=3,rowspan=2,sticky=S+N)
Label(master, text="Second").grid(row=3)


master.mainloop()
#######
'''
Para alinear las etiquetas al borde izquierdo, usas W(west)
N, S, E, W. 

'''
#######
'''
Label(master, text="First").grid(row=0, sticky=W)
Label(master, text="Second").grid(row=1, sticky=W)

e1 = Entry(master)
e2 = Entry(master)

e1.grid(row=0, column=1)
e2.grid(row=1, column=1)

'''

#La opcion de columnspan es usada para hacer que un wodget abarque mas de una columna y rowspan para que abarque mas de una fila
'''
from tkinter import *

master = Tk()

Label(master, text="First").grid(row=0)
Label(master, text="Second").grid(row=1)

e1 = Entry(master)
e2 = Entry(master)

e1.grid(row=0, column=1)
e2.grid(row=1, column=1)

Button(master,text="Boton").grid(row=2,columnspan=2,sticky=S+N)
Button(master,text="Boton").grid(row=2,column=3,rowspan=2,sticky=S+N)
Label(master, text="Second").grid(row=3)



master.mainloop()
'''