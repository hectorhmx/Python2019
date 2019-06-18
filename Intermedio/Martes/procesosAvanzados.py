#####Primero vamos a heredar de la clase hilo
import multiprocessing
import ctypes
from time import time
suma = None
class HiloConLock(multiprocessing.Process):
    def __init__(self,lock,n1,n2):
        """
        Obtendremos de aqui la barreara, y creando nuestro propio constructor
        """
        super().__init__() ###Llamamos al padre de esta funcion
        self.n1 = n1
        self.n2 = n2
        self.lock=lock
    def run(self):
        global suma
        """
        Method override, estamos redefiniendo el método run que existe en threading
        de este modo podemos modificar como se ejecutara el hilo
        """
        sum = 0
        for i in range(self.n1,self.n2):
            sum+=i
        with self.lock:
            suma.value+=sum

if __name__ == "__main__":
    ##Definimos el número 1000de hilos
    numHilos = 5

    ###Definimos la lista de hilos
    listaHilos = []
    ## Definimos un lock y un contador compartido 
    lock = multiprocessing.Lock()
    suma = multiprocessing.Value(ctypes.c_longlong,0)
    numMax=100000000
    limitador = numMax//numHilos###tamaño que le corresponde
    ###Para este caso, numMax debe ser multiplo de numero de hilos

    cont = 0
    ###Creamos los hilos
    for i in range(numHilos):
        hilo = HiloConLock(lock,cont,cont+limitador)
        cont+=limitador
        listaHilos.append(hilo)


    ###Empezamos todos los hilos
    inicioCP = time()
    for i in listaHilos:
        i.start()
    ###Hacemos que todos terminen
    for i in listaHilos:
        i.join()
    finalCP = time()
    timepoCP = finalCP - inicioCP # tiempo con procesos
    print("Suma paralela",suma.value)
    print('Tiempo con procesos =>',timepoCP)
    
    inicioCP = time()
    sumaReal = 0
    for i in range(numMax):
        sumaReal+=i
        finalCP = time()
    print("Suma real    ",sumaReal)
    timepoCP = finalCP - inicioCP # tiempo sin procesos
    print('Tiempo serial =>',timepoCP)

