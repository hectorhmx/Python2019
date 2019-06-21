from funciones import contar, factorial, agregarLista
from threading import Thread
from time import time

###Definimos los hilos, estos ejecutarán las funciones
hilo1 = Thread(target=contar)
hilo2 = Thread(target=factorial)
hilo3 = Thread(target=agregarLista)

###Calcularemos el tiempo
inicio = time()
hilo1.start() # start hace que el hilo comience a realizar la función que tiene asociada
hilo2.start()
hilo3.start()

# join hace que la ejecución del programa espere a que los hilos terminen 
# de realizar las funciones que tienen asociadas para podedr continuar
hilo1.join()
hilo2.join()
hilo3.join()
final = time()
print('Todos los hilos terminaron de realizar su respectivas tareas')
print('Tiempo transcurrido =>',final-inicio)
