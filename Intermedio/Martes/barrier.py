#####Primero vamos a heredar de la clase hilo
import threading
from time import sleep

class HiloConBarrera(threading.Thread):
    def __init__(self,barrier,id):
        """
        Obtendremos de aqui la barreara, y creando nuestro propio constructor
        """
        self.barrier=barrier
        self.id=id
        super().__init__() ###Llamamos al padre de esta funcion
    def run(self):
        """
        Method override, estamos redefiniendo el método run que existe en threading
        de este modo podemos modificar como se ejecutara el hilo
        """
        self.trabajarPesado()
        print("Hilo:{} Alcanzó la barrera ".format(self.id))
        self.barrier.wait() ###Hacemos que espere a los otros hilos para continuar
        print("Hilo:{} Volvio a trabajar".format(self.id))
        self.trabajarPesado()
    
    def trabajarPesado(self):
        for i in range(5):
            #print("Hilo: {} esta trabajando".format(self.ident)) ##identificador dado por python
            print("Hilo: {} esta trabajando".format(self.id)) ##identificador dado por python
            sleep(3)

if __name__ == "__main__":
    ##Definimos el número 1000de hilos
    numHilos = 5

    ###Definimos la lista de hilos
    listaHilos = []
    ###Definimos la barrera y le pasamos el número de 
    # hilos necesarios para pasar la barreara
    barrera = threading.Barrier(numHilos)

    ###Creamos los hilos
    for i in range(numHilos):
        hilo = HiloConBarrera(barrera,i)
        listaHilos.append(hilo)
    
    ###Empezamos todos los hilos

    for i in listaHilos:
        i.start()
    

    ###Hacemos que todos terminen
    for i in listaHilos:
        i.join()

##Hacer un programa que calcule la suma desde 1 hasta n con hilos.
###dividiendo el conjunto entre el número de hilos

### a modo de que modifique el constructor y este me sume 1 hasta m de m a z, de z a n
###