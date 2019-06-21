from multiprocessing import Process
from time import time
from funciones import contar, factorial, agregarLista

# print(multiprocessing.cpu_count())

if __name__ == '__main__':
    """
    inicioSP = time()
    contar()
    factorial()
    agregarLista()
    finalSP = time()
    timepoSP = finalSP - inicioSP # tiempo sin procesos
    print('Tiempo sin procesos =>',timepoSP)
"""

    ##Para saber el número de procesos posibles:
    ##len(os.sched_getaffinity(0))
    proceso1 = Process(target = contar)
    proceso2 = Process(target = factorial)
    proceso3 = Process(target = agregarLista)

    inicioCP = time()
    proceso1.start()
    proceso2.start()
    proceso3.start()

    proceso1.join()
    proceso2.join()
    proceso3.join()
    finalCP = time()

    timepoCP = finalCP - inicioCP # tiempo con procesos


    print('Tiempo con procesos =>',timepoCP)