from tkinter import ttk
from tkinter import *
import sqlite3

class Product:
    db_name = 'Productos.db'
    def __init__(self, window):
        self.wind = window
        self.wind.title('SQL Graficals')
        frame = LabelFrame(self.wind, text ='Registra un nuevo producto' )
        frame.grid(row = 0, column = 0, columnspan = 3, pady = 20)

        ### Caja de entrada
        Label(frame, text = 'Nombre: ').grid(row = 1, column = 0)
        self.name = Entry(frame)
        self.name.grid(row = 1, column = 1)

        ### Price Input
        Label(frame, text = 'Precio: ').grid(row = 2, column = 0)
        self.price = Entry(frame)
        self.name.focus()
        self.price.grid(row = 2, column = 1)

        ### Botones
        ttk.Button(frame, text = 'Salvar dato', command = self.add_prodcut).grid(row = 3, columnspan = 2, sticky = W + E)        ###Fila, columna y todo el ancho disponible este a oeste

        ###Boton de mensaje
        self. message = Label(text = '', fg = 'green')
        self.message.grid(row = 3, column = 0, columnspan = 2, sticky = W + E)
        
        ###Table
        self.tree = ttk.Treeview(height= 10, columns = 2)
        self.tree.grid(row  = 4, column = 0, columnspan = 2 )
        self.tree.heading('#0',text = 'Nombre', anchor = CENTER)
        self.tree.heading('#1',text = 'Precio', anchor = CENTER)
        
        ##
        ttk.Button(text = 'Borrar', command = self.delete_product).grid(row=5, column = 0, sticky = W+E)
        ttk.Button(text = 'Editar', command = self.edit_product).grid(row=5, column = 1, sticky = W+E)
        ##
        self.get_product()
        
    def run_query(self,query,parameters = ()):
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            result = cursor.execute(query, parameters)
            conn.commit()
        return result

    def get_product(self):
        records = self.tree.get_children() ##Obtener todos los datos de la tabla
        for element in records: ##Limpiando la tabla
            self.tree.delete(element)
        ##Obteniendo datos
        query ='SELECT * FROM Producto'
        db_rows = self.run_query(query)
        print(db_rows)
        for row in db_rows:
            print(row)
            self.tree.insert('',0, text = row[1], values = row[2])
    
    def validacion(self):
        ##longitud del usuario y el precio
        ##Validarlos através de operador ternario
        return len(self.name.get()) !=0 and len(self.price.get()) != 0

    def add_prodcut(self):
        if self.validacion():
            query = 'INSERT INTO Producto VALUES (NULL,?,?)'
            parameters = (self.name.get(), self.price.get())
            self.run_query(query, parameters)
            #print('Dato salvado :D')
            #print(self.name.get())
            #print(self.price.get())
            self.message['text'] = 'Producto {} Agregado correctamente'.format(self.name.get())
            self.name.delete(0, END)
            self.price.delete(0, END)
        else:
            #print("Nombre y precio requeridos")
            self.message['text'] = 'Nombre y precio requeridos'
        self.get_product()

    def delete_product(self):
        self.message['text'] = ''
        try:
            self.tree.item(self.tree.selection())['text'][0]
        except IndexError as e:
            self.message['text'] = 'Please Select a Record'
            return 
        self.message['text'] = ''
        query = 'DELETE FROM Producto WHERE nombre = ?'
        name = self.tree.item(self.tree.selection())['text']
        self.run_query(query, (name, ))
        self.message['text'] = 'Record {} Eliminado Satisfactoriamente'.format(name)
        self.get_product()

    def edit_product(self):
        self.message['text'] = ''
        try:
            self.tree.item(self.tree.selection())['text'][0]
        except IndexError as e:
            self.message['text'] = 'Please Select a Record'
            return 
        name  = self.tree.item(self.tree.selection())['text']
        old_price = self.tree.item(self.tree.selection())['values'][0]
        self.edit_wind = Toplevel()
        self.edit_wind.title = 'Edit Product'
        ##Old Name
        Label(self.edit_wind, text = 'Nombre Antiguo: ').grid(row = 0, column = 1)
        Entry(self.edit_wind, textvariable = StringVar(self.edit_wind, value=name), state = 'readonly').grid(row =0, column = 2)

        ##New Name
        Label(self.edit_wind, text = 'Precio Nuevo: ').grid(row =1, column = 1)
        new_name = Entry(self.edit_wind)
        new_name.grid(row =1, column =2)

        ##old Price
        Label(self.edit_wind, text = 'Precio Antiguo').grid(row =2, column=1)
        Entry(self.edit_wind, textvariable = StringVar(self.edit_wind, value = old_price), state = 'readonly').grid(row = 2, column=2)
        
        ##New Price
        Label(self.edit_wind, text = 'Nuevo Nombre').grid(row =3, column=1)
        new_price = Entry(self.edit_wind)
        new_price.grid(row = 3, column=2)

        ###Botton nuevo
        Button(self.edit_wind, text = 'Actualizar', command = lambda: self.edit_records(new_name.get(), name, new_price.get(), old_price)).grid(row =4, column = 2, sticky = W)
    
    def edit_records(self, new_name, name,new_price,old_price):
        query = 'UPDATE Producto SET Nombre = ?, Precio = ? WHERE Nombre = ? AND Precio = ?'
        parameters = (new_name, new_price, name, old_price)
        self.run_query(query, parameters)
        self.edit_wind.destroy()
        self.message['text'] = 'Record {} update Succesfoly'. format(name)
        self.get_product()

if __name__ == '__main__':
    window = Tk()
    app = Product(window)
    window.mainloop() ##Ejecucion en la ventana