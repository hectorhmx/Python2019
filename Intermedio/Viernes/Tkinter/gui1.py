# ROOT Y LABEL

from tkinter import *
# Generalmente tkinter se importa de esta forma
# Para tener acceso a sus servicios

root = Tk() # Clase Tk
# Se genera una ventana raiz # root window
# Nos permite tratar a los widgets en una ventana como objetos
# Lo que nos sale es la instancia de la clase Tk

widget = Label(root, text = 'Mi primer GUI!!') # Clase Label
# root es el widget padre
# Crea una instancia de la clase Label
# Crea un Label -> Cuadro con texto
# No se pondrá hasta que nosotros indiquemos
# Podemos cambiar la longitud del texto y pack cambiará la longitud de la ventana

widget.pack()
# Coloca el nuevo Label en el widget padre (root en este caso)

root.mainloop()
# Despliega la interfaz en monitor e inicia espera por eventos