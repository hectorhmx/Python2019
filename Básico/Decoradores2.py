#3
# decorador que agrega un mensaje con el nombre de la funcion
def nombre(funcion):
    def decorada(*parms):    # * se usa para indicar que la funcion puede tener 0 o mas parametros
        # acciones nuevas de la funcion
        print("Se ha iniciado la funcion %s"%(funcion.__name__))
        return funcion(*parms)  #funcion original
    return decorada


def cubo(n):
    print (n**3)

@nombre         # se puede indicar el decorador usando @ para que se llame solo
def suma(a,b):
    print (a+b)



F=nombre(cubo)    # sin usar @
F(2)

suma(3,7)         # usando @
