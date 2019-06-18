from funciones import contar, factorial, agregarLista
from threading import Thread
from time import time

hilo1 = Thread(target=contar)
hilo2 = Thread(target=factorial)
hilo3 = Thread(target=agregarLista)

inicio = time()
hilo1.start() # start hace que el hilo comience a realizar la función que tiene asociada
hilo2.start()
hilo3.start()

# join hace que la ejecución del programa espere a que los hilos terminen 
# de realizar las funciones que tienen asociadas para podedr continuar
hilo1.join()
hilo2.join()
hilo3.join()

print('Todos los hilos terminaron de realizar su respectivas tareas')

final = time()
print('Tiempo transcurrido =>',final-inicio)