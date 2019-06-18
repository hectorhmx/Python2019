from funciones import agregarLista, factorial, pedirValores
from time import time
from threading import Thread

inicioSH = time()
pedirValores()
factorial()
agregarLista()
finalSH = time()
timepoSH = finalSH - inicioSH # tiempo sin hilos
print('Tiempo sin hilos =>',timepoSH)

"""hilo1 = Thread(target=pedirValores)
hilo2 = Thread(target=factorial)
hilo3 = Thread(target=agregarLista)

inicioCH = time()
hilo1.start()
hilo2.start()
hilo3.start()

hilo1.join()
hilo2.join()
hilo3.join()
finalCH = time()

timepoCH = finalCH - inicioCH # tiempo con hilos

print('Tiempo con hilos =>',timepoCH)"""