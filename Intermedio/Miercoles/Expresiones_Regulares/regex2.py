"""
patron.findall(texto)

Retorna una lista que contiene todos las concordancias
generadas. En caso de existir grupos, retorna una lista 
con los grupos sin incluir el 0


patron.finditer(texto)

Retorna un iterador que va a ir retornando objetos Match
de cada concordancia.

"""

import re

texto = """Mi teléfono es 5520391428 y el de mi jefe es 5539482039,
El de mi hermana es 5529283847 y el de mi mamá es 5220391820."""

patron1 = re.compile(r"\d{2}\d{8}")

lista = patron1.findall(texto)
print(lista)

patron2 = re.compile(r"(\d{2})\d{8}")
lista = patron2.findall(texto)

for objMatch in patron2.finditer(texto):
	print(objMatch)
	print(objMatch.group())
	print(objMatch.group(1))








