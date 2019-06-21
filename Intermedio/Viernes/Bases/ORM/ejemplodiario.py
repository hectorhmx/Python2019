##ejemplo de Diario
from peewee import *
import datetime
from collections import OrderedDict
import sys

db = SqliteDatabase('diary.db')



class Entry(Model):
	content = TextField()##Bonche de Texto
	timestamp = DateTimeField(default = datetime.datetime.now) ##DEFAULT SYSDATE

	class Meta:
		database = db

def create_and_connect():
	db.connect()
	db.create_tables([Entry], safe=True) ##Cada ves que se llame no repita cosas creadas

def menu_loop():
	"""Show Menu"""
	choice = None
	while choice !='q':
		print("Presione 'q' para salir")
		for key, value in menu.items():
			print("{}) {}".format(key,value.__doc__)) ##tomar como valor lo que este dentro del docstring
		choice = input("Action: ").lower().strip()

		if choice in menu:
			menu[choice]()
	pass

def add_entry():
	"""Agregar una entrada"""
	print("Escribe tus pensamientos\nPresion ctrl + D para finalizar")
	data = sys.stdin.read().strp()
	if data:
		if input("Quieres salvar los cambios[Y/N]\n").lower
	pass

def view_entries():
	"""Mostrar todas las entradas"""
	print("Mostrar una entrada")
	pass
def delete_entry():
	"""Borrar entrada"""
	print("Borrando una entrada")
	pass

menu = OrderedDict([
	('a', add_entry),
	('v', view_entries),
	('d', delete_entry)
	])

if __name__ == '__main__':
	create_and_connect()
	menu_loop()