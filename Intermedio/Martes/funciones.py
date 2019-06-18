from time import time
def contar(): # Va ir asignando la variable num a cada numéro entero que hay antes de n, y lo va a retornar al finalizar
    num = 0
    for elemento in range(11999999):
        num = elemento**2
    print('Terminando de contar')

def factorial(): # Función que calcula el factorial de n utilizando un ciclo for y retorna el resultado
    resultado = 1
    for i in range(1,100000):
        resultado*=i
    print('Terminando de realizar factorial')


def agregarLista(): # Función que agrega n elementos a una lista y la retorna
    lista = []
    for i in range(10000000):
        lista.append(i**2)
    print('Terminando de agregar a lista')

def countTime(func):
    inicio = time()
    func()
    final = time()
    print('Tiempo transcurrido =>',final-inicio)

if __name__ == '__main__':

    ##Intentar que las funciones tomen lo mismo

    inicioGen = time()
    countTime(contar)
    countTime(factorial)
    countTime(agregarLista)
    finalGen = time()
    print('Tiempo total = >',finalGen-inicioGen)