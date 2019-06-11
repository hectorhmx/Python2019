"""
1
Las expresiones generadoras son muy útiles: son similares las list comprehensions
pero en lugar de devolver una lista devuelven un objeto sobre el que se puede iterar.
La sintaxis de los generadores es la misma que la de la Comprensión de listas pero
usando paréntesis en vez de corchetes
"""
lista = [1,2,3,4]
listac = [n**2 for n in lista]
print(listac)
#####################################3
lista2 = (n**2 for n in lista)
print(type(lista2))
print(lista2)
################Creando tu propio generador sencillo################################################
def mi_generador(inicio,fin,paso):
    while(inicio <= fin):
        yield inicio
        inicio +=paso
# Generando numeros pares
for numero in mi_generador(0, 100, 2):
    print(numero)