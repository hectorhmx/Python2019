##########################¿Qué excepciones hay?###############

#NOTA: Es recomendable que leas este documento seleciconando de la barra superior la sección View->Word Wrap , ya que los comentarios realizados en este documento son de una línea

""" Las excepciones se presentan durante la ejecución del programa 

Ejemplo 1: Cuando se divide entre 0

x = 5*(6/0)
6/0 no es posible efectuarse, por lo que si integramos eso en nuestro programa nos enviará un error del tipo: 'ZeroDivisionError: division by zero'


Ejemplo 2 : Utilizar variables no definidas
y = 1 + numero*3
'numero' no ha sido definida, por lo que no es posible efectuar esa operación indicada, por lo tanto genera un error de tipo: ‘NameError: name 'numero' is not defined’


Ejemplo 3: Multiplicar variables de tipo cadena con variables de tipo entero
z = 2+ '7'
'7' es una cadena que contiene al número 7, sin embargo por haber sido definida así, no es posible que se opere con el número 2. Por esta razón genera una excepción de tipo: ‘TypeError: unsupported operand type(s) for +: 'int' and 'str'’


"""

"""Manejo de excepciones """ 
#Definimos una función que reciba un número. Sin try, except
def excepcion_probable(numero):
    numero = float(numero)
    print("La raíz cuadrada del número", numero, "es:", numero ** 0.5)
    print("Buen día.")
# Value error si le pongo una cadena. ValueError: could not convert string to float: 'hola'	
#TypeError si coloco un número complejo: TypeError: can't convert complex to float

# ‘NameErroR si utilizo una varible en lugar de un número:NameError: name 'hola' is not defined


#Definimos una función que reciba un número. Con try, except

def excepcion_una(numero):
	try:
		numero = float(numero)
		print("La raíz cuadrada del número", numero, "es:", numero ** 0.5)
	except:
		pass
	print("Buen día.")
#Este try-except me permite que no gener error si ingreso una cadena o un complejo
#PEEEEROOOOOOO.... Capturar las excepciones sin dejar evidencia de que ocurrieron no es una buena idea. Realmente no se gestionan los errores sino que simplemente se esconden, arrojando muy probablemente resultados inesperados y aún más errores posteriormente.

#Una técnica muy común para la gestión de errores es el uso de "banderas". que por lo general son objetos de tipo bool que cambian de valor en caso de que un evento ocurra, pero en este caso manejaremos las excepciones por su tipo

#La expresión except puede ser utilizada de forma tal que ejecute código dependiendo del tipo de error que ocurra de una forma muy similar a elif.

def excepciones_varias(numero):
    """ Ejemplo de control de excepciones para diversos errores identificados.
        En caso de que ocurra un error inesperado, se desplegará una advertencia.
        El programa pedirá un número y desplegará la raíz cuadrada de dicho número."""
    try:
        numero = float(numero)
        print("La raíz cuadrada del número", numero, "es:", numero ** 0.5)
    except TypeError:
        print("Ocurrió un error previsto. Tu tipo de dato no es válido")
        print('Características del error:',TypeError, TypeError.__doc__)
        #TypeError sólo me muetsra la clase de error
        #TypeError.__doc__ me da más información sobre la escepción
    except:
        print("¿Qué está pasando? No sé qué hiciste u.u")
    print("Buen día, regresa pronto")
# agregar este except para que capture cuando el usuario ponga cadenas
    """except ValueError:
    	print("¿Me diste una cadena en lugar de un número?")
    	print('Características del error:',ValueError,ValueError.__doc__)"""

""""Otra manera de poner lo anterior es:
def excepciones_varias(numero):
    try:
        numero = float(numero)
        print("La raíz cuadrada del número", numero, "es:", numero ** 0.5)
    except TypeError:
        print("Ocurrió un error previsto. Tu tipo de dato no es válido")
        print('Características del error:',TypeError, TypeError.__doc__)
    except ValueError:
    	print("¿Me diste una cadena en lugar de un número?")
    	print('Características del error:',ValueError,ValueError.__doc__)
    except:
        print("¿Qué está pasando? No sé qué hiciste u.u")
    print("Buen día, regresa pronto")
   
Otra manera es:

def excepciones_varias(numero):
    try:
        numero = float(numero)
        print("La raíz cuadrada del número", numero, "es:", numero ** 0.5)
    except (TypeError,ValueError):
        print("Ocurrió un error previsto.")
		print("Pudo haber sido:", TypeError)
		print("o de lo contrario: ", ValueError)
    except:
        print("¿Qué está pasando? No sé qué hiciste u.u")
    print("Buen día, regresa pronto")
 """



#Uso de else y finally.Además de except, Python cuenta con otros dos recursos que completan la gestión de excepciones.La expresión 'else'. Del mismo modo que un if, la expresión else se ejecuta en el caso de que no se genere una excepción.

def excepciones_elsefinally(numero):
    """ Ejemplo de control de excepciones para diversos errores.
        Desplegará el cuadrado de dicho número.
        En caso de ocurrir una excepción se despelgará el mensaje de error."""
    ocurre_error = True # creamos una bandera, la cual se convertirá en False cuando no haya ocurrido ningún error
    try:
        numero = float(numero)
        print("\nLa raíz cuadrada del número", numero, "es:", numero ** 0.5)
    except (ValueError, TypeError) as excepcion:
        print("\nMensaje de error. Características del error:", excepcion)
    except:
        print("\n¡No sé qué pasó! D:")
    else:
        print("\nNo hubo errores. Eres el mejor 7u7")
        ocurre_error = False # en caso de no cometerse ninguna excepción, la bandera adquiere el valor de False, por lo que al entrar en el ciclo de finally imprimirá en pantalla lo corresponciente al else
    finally:
        if ocurre_error:
            print("\nLo siento, cometiste un error, intenta de nuevo")
        else:
            print("\n¡Yeih! Sí sabes qué es necesario para calcular la raíz cuadrada de un número. ")
    print("\n\t***Que tengas buen día, gracias por tu preferencia***")

#Levantar excepciones son 'raise'.En ciertas ocasiones es posible identificar una situación en la que cierta condición provocará un error. En ese caso se puede levantar una excepción antes de que el error ocurra y emitir un mensaje correspondiente.La expresión raise se utiliza para levantar excepciones definidas por el programador.

def levanta_excepcion(numero):
	ocurre_error = True
	try:  
		if numero < 0:
			raise TypeError
		print("\nLa raíz cuadrada del número", numero, "es:", numero ** 0.5)
	except TypeError:
		
		print("Ocurrió una excepción identificada. Características:", TypeError)
	except ValueError:
		print("Ocurrió un error. características")
	except:
		print("Código rojo, código rojo,¡No sé qué pasó!")
	else:
		print("No hubo errores.")
		ocurre_error = False
	finally:
		if ocurre_error:
			print("ufff, algo salió mal")
		else:
			print("oh, yeah, lo lograste.")