from peewee import *
db = SqliteDatabase('Basepew.db')

class Pais(Model):
	nombre = CharField()
	continente = CharField()
	lengua = CharField()
	moneda = CharField()

	class Meta:
		database = db

def create_connect():
	db.connect()
	db.create_tables([Pais], safe = True)

def insert():
	EUA = Pais(nombre='Estados Unidos America', continente='America', lengua='Ingles', moneda ='Dolar')
	EUA.save()
	mexico = Pais(nombre='Estados Unidos Mexicanos', continente='America', lengua='Español', moneda ='Peso Mexicano')
	mexico.save()

create_connect()
insert()
#EUA = Pais.create(nombre='Estados Unidos America(EUA)', continente='Americano', lengua='Ingles',moneda='Dolar')
#EUA.save()