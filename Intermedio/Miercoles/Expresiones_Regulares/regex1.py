
"""
patron.search(texto)

Genera un objeto match de la primer concordancia
encontrada en el texto, en caso de no haber ninguna
concordancia, retorna None 


patron.sub(rempl, texto)

Genera una cadena que reemplace las concordancias
por un valor de reemplazo preestablecido

"""

"""
match.group(n)
# Retorna el grupo n del match
"""

"""
match.groups()
# retorna una tupla con los grupos
"""

import re

texto = "Mi teléfonoes 5537867029 y el de mi hermana es 5539484920"

#print("hola\ncomo\nestas?")
#print(r"hola\ncomo\nestas?") # raw string
# ignora los caracteres de escape -> \n o \t

patron = re.compile(r"(\d{2})(\d{8})")

print(type(patron))

# Si cambiamos el patron a uno que no genere
# match, patron va a ser None

objMatch = patron.search(texto)

print(objMatch)
print(type(objMatch))

# Una vez creado el objeto match, podemos
# acceder a los diferentes grupos que lo
# conforman
print(objMatch.group()) #print(match1.group(0))
print(objMatch.group(1))

textoNuevo = patron.sub("TELEFONO", texto)

print(textoNuevo)










