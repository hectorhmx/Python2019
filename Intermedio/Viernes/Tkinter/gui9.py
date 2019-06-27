# POO
"""
Botón que termina el programa al ser apretado
"""
from tkinter import *

'''
raiz = Tk()
Button(raiz, text='Salir', command=raiz.quit).pack()
raiz.mainloop()
'''


class BtnTerminar(Frame):
    # Parámetros por default
    def __init__(self, padre=None):
        Frame.__init__(self, padre)
        self.pack()
        Button(self, text='Salir', command=self.terminar,
               bg='#E85713', fg='#42425C').pack(expand=YES, fill=BOTH)
        # padre = self
        # la instancia de BtnTerminar es el widget padre de el boton

    def terminar(self):
        Frame.quit(self)  # termina el mainloop


if __name__ == '__main__':
    '''boton = BtnTerminar()
    boton.pack(expand=YES, fill=BOTH)'''
    BtnTerminar().pack(expand=YES, fill=BOTH)
    '''for i in range(10):
        BtnTerminar().pack(expand=YES, fill=BOTH)'''
    Button(text = 'HOLA').pack()
    mainloop()
