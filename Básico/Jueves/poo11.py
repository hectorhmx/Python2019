class MiLista(list):  # Heredamos de la clase list

    def append(self, objeto):  # Modificamos funcionamiento de append
        # Cuand usemos append va a hacer una impresión
        print('Agregando al final')
        # Se va a mandar a llamar el método append de list
        list.append(self, objeto)


# lista = list((1,4,2,4))
lista = MiLista((1, 4, 2, 4))
lista.append(1)
lista.append(2)
print(lista)
