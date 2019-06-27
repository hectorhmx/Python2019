# ROOT Y LABEL

from tkinter import *

# La interfaz siempre va a tener una ventana raiz, ya sea que
# la creemos explicitamente con Tk() o que python la ponga
# por default como en este ejemplo

label1 = Label(text = 'Texto..')
label2 = Label(text = ' Mas texto..', bg = 'red')
label3 = Label()

label3.config(text = 'Aún más texto....', fg = 'yellow', bg = 'black')
# Podemos modificar los atributos de un widget despues de
# haberlo creado

label1.pack(side = LEFT, fill = BOTH, expand = YES)
label2.pack(side = RIGHT, fill = BOTH, expand = YES)
#fill - rellena sus dimensiones dadas por el empaquetador o solo se queda con sus dimensiones minimas
#expand - el widget se expande para llenar cualquier espacio que no se utilice de otra manera en el elemento primario del widget.

label3.pack()
#Si no usamos pack, el widget no se coloca

mainloop()
# Si no iniciaramos el loop no se desplegaría nada
