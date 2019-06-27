 # EVENTOS

from tkinter import *


# Al activarse un evento, se manda a llamar a la función asociada pasando
# como parámetro el objeto evento
# este objeto tiene argumentos útiles para saber información
# del evento en cuestión

def imprimirPos(event):
    print('Eje x: %s    Eje y: %s' % (event.x, event.y))


def moviendo(event):
    print('Moviendo..', end='    ')
    imprimirPos(event)


def guardarTecla(event):
    print('Se obtuvo', event.char)


def terminar(event):
    print('Terminando...')
    raiz.quit() # quit termina el mainloop

def enter(event):
    print('Enter!!')

def imprimirPos(event):
    print('Eje x: %s    Eje y: %s' % (event.x, event.y))

raiz = Tk()
label = Label(raiz, text='Eventos', bg='blue')
btn1=Button(raiz,text="btn1")
btn2=Button(raiz,text="btn2")
btn1.pack()
btn2.pack()

entry =Entry(raiz)
entry.pack()

label.config(height=10, width=20)
label.config(font=('courier', 20, 'bold'))
label.pack(fill=BOTH, expand=YES)



#entry.bind('<Key>', guardarTecla)
#entry.bind('<KeyPress>', guardarTecla)
#entry.bind('<Return>', enter)
#btn2.focus()

'''
label.bind('<Button-1>', imprimirPos) #al hacer click

label.bind('<B1-Motion>', moviendo) #al moverse con click
label.bind('<Button-3>', lambda event: print('Click izq')) #click izquierdo

label.bind('<Double-1>', terminar) ##doble click
'''
mainloop()
