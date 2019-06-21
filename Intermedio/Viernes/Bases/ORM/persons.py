from peewee import *
from datetime import date
db = SqliteDatabase('Persons.db')
###Definicion de las clases para crear las tablas
### Correspondientes a la base de datos

class Person(Model):
	name = CharField()
	birthday = DateField()
	is_relative = BooleanField()

	class Meta:
		database = db

class Pet(Model):
	owner = ForeignKeyField(Person, related_name = 'pets_fk') ##Declarar uan lalve foranea
	name = CharField()
	animal_type = CharField()

	class Meta:
		database = db
############################################
def create_and_connect():
	db.connect()
	db.create_tables([Person, Pet], safe=True)


def create_family_members():
	uncle_tommy = Person(name="Tommy", birthday=date(2000,11,11), is_relative=True)
	uncle_tommy.save()

	grandma_ana = Person.create(name="Ana", birthday=date(1960, 11,11), is_relative=False)
	grandma_rosa = Person.create(name="Rosa", birthday=date(1960, 11,11), is_relative=False)	

	tommys_dog = Pet.create(owner=uncle_tommy,name = "Fido", animal_type="Perro")
	anas_cat  =Pet.create(owner=grandma_ana,name = "Charlie", animal_type="Gato")

	##Actualizar un registro
	tommys_dog.name = "Jett"
	tommys_dog.save()

def get_family_members():
	for person in Person.select(): ##select * from Person
		print("ID: {} Nombre: {} Fecha de Nacimiento: {}".format(person.id,person.name, person.birthday))

def get_family_member_birthday():
	grandma_rosa = Person.select().where(Person.name == "Rosa").get()
	##family_member = Person.get(Person.name ==name) ##Para un unico registro
	print("La abuela Rosa cumple el: {}". format(grandma_rosa.birthday))

def delete_pet(name):
	query = Pet.delete().where(Pet.name ==name)
	borrados = query.execute() ##Para ejecutar el delete y saber cuantos fueron borrados
	print("Se borraron: ", borrados)

create_and_connect()
#create_family_members()
get_family_members()
#get_family_member_birthday()
delete_pet("Charlie")
