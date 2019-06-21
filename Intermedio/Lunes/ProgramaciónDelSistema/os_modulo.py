"""
os es el más grande de los dos módulos del sistema central.
Contiene todas las llamadas habituales al sistema operativo que usa en programas C y scripts de shell.
Sus llamadas tratan con directorios, procesos, variables de shell y similares. Técnicamente, este módulo proporciona 
herramientas POSIX, un estándar portátil para llamadas al sistema operativo, junto con herramientas de procesamiento 
de directorios independientes de la plataforma como el módulo anidado os.path.

Operacionalmente, os sirve como una interfaz en gran parte portátil para las llamadas al sistema de su computadora:
los scripts escritos con os y os.path generalmente pueden ejecutarse sin cambios en cualquier plataforma.

"""
os.getpid() 
# la función os.getpid proporciona el ID del proceso del proceso de llamada (un identificador único definido por 
#el sistema para un programa en ejecución, útil para el control de procesos y la creación de nombres únicos),
#con ps se ven los procesos existentes desde la etrminal
os.getcwd()
# y os.getcwd devuelve el directorio de trabajo actual. El directorio de trabajo actual es donde se asume que los 
#archivos abiertos por su script viven, a menos que sus nombres incluyan rutas de directorio explícitas. 

os.path.isdir('ruta') #Muestra si la ruta es un directorio.
os.path.isfile('ruta') #Muestra si la ruta es un archivo

#Nos permite saber en que entorno o sistema operativo nos encontramos
print(os.name) # imprime posix, que significa' Interfaz Portátil de Sistema Operativo para Unix.'
#Este metodo nos regresa una tupla con las carcteristicas de nuestro sistema
print(os.uname())

#Nos regresa una lista con el contenido de la carpeta que indiquemos
print(os.listdir(".."))

#La función mkdir () crea un directorio. Devuelve un error si el directorio padre no existe. 
#Si también desea crear el directorio padre, debería usar makedirs () :
os . mkdir ( 'temp' )  # crea un directorio temporal dentro del directorio actual 
os . makedirs (" / tmp / temp / temp ") 
#Una vez creado, puede eliminar un directorio vacío con rmdir () :
os . mkdir ( '/ tmp / temp' ) 
os . rmdir ( '/ tmp / temp' )
#Ejemplo, crear una ruta multiplataforma utilizando el símbolo separador adecuado:
import os
import os.path
os.path.join(os.sep, 'home', 'user', 'work')
#Os.path implementa funciones para trabajar sobre los nombres de rutas de archivos
#os.sep da el carácter tilizado por el S.O. para separar los componentes de la ruta. / para POSIX, \ para Windows
# si usamos os.path.join ya podemos concatenar la ruta
#'/home/user/work'

#Limpiar el intérprete de Python
import os #importamos os
os.system('clear') #para linux
os.system('cls') #para windows
#Si el resultado de la ejecución es 0, finali´zó con éxito
#Ejemplos de comandos a usar: pwd (ruta actual), woami (nomnre del usuario), ls (enlistar)
#ps (procesos) , mkdir(crear una carpeta), touch (clear un archivo), top (procesos actuales en tiempo real), etc

#Ejercicio
"""Con lo aprendido en los módulos Sys y Os crear un menú con las siguientes opciones
                         1.-Crear carpeta
                         2.-Ver contenido de la carpeta
                         3.-Indicar que sistema operativo es y saludar al usuario.
                         """
 #Solución
 import sys,os # importamos ls módulos
 eleccion ="1" #LE damos un valor predefinido a la variabel elección
 while eleccion != "4": #SMientras eleccion sea diferente de 4, es decir, salir, se  continuará mostrando el menú
 	#Imprime las opciones del menú
 	print('\n1.-Crear una carpeta\n2.-Ver contenido de la carpeta,\n3.-Sistema Operativo de la computadora\n4.-Salir')
 	eleccion = input("Selecciona 1,2 ,3 o  4") #Se guarda la la respuesta del ususario en la variable eleccion
 	if eleccion =="1": # si eleeccion es igual a 1,
 		os.mkdir('nueva') # se crea una carpeta
 		print("Se ha creado una carpeta llamada'nueva'\n") # ys e anuncia a l usuario lo ocurrido
 	elif eleccion == "2": # si eleccion es igual a 2
 		os.system('ls') # se enlista el contenido, puede ser de esta amnera o con os.listdir()
 	elif eleccion == "3": # si la eleecion es igual a 3
 		print(sys.platform) # se imprimir el S.O.

#Si deseas conocer más herramientas de Sys y Os, entra en la documentación en : https://docs.python.org/3/library/os.html
#En estos documentos encontrarás:


os.path.abspath( camino ) 
"""Devuelve una versión normalizada de la ruta de acceso de ruta . En la mayoría de las plataformas, esto es equivalente
 a llamar a la función normpath()de la siguiente manera: .normpath(join(os.getcwd(), path))

 Cambiado en la versión 3.6: Acepta un objeto similar a una ruta ."""

 os.path.basename( camino ) 
"""Devuelve el nombre base de la ruta de acceso de la ruta . Este es el segundo elemento del par devuelto al pasar la 
ruta a la función split(). Tenga en cuenta que el resultado de esta función es diferente del programa de nombre base de Unix ; donde el nombre base para '/foo/bar/'devoluciones 'bar', la basename()función devuelve una cadena vacía ( '').

Cambiado en la versión 3.6: Acepta un objeto similar a una ruta ."""

os.path.commonpath( caminos ) 
"""Devuelva la ruta secundaria más larga de cada ruta de acceso en las rutas de secuencia . Aumente ValueError si las 
rutas contienen tanto rutas de acceso absolutas como relativas, o si las rutas están vacías. A diferencia
 commonprefix(), esto devuelve una ruta válida.
Disponibilidad : Unix, Windows.Nuevo en la versión 3.5.Cambiado en la versión 3.6: Acepta una secuencia de objetos 
similares a rutas ."""

os.path.commonprefix( lista ) 
"""Devuelve el prefijo de ruta más largo (tomado carácter por carácter) que es un prefijo de todas las rutas en la 
lista . 
Si la lista está vacía, devuelve la cadena vacía ( '').

Nota Esta función puede devolver rutas no válidas porque funciona un carácter a la vez. Para obtener una ruta válida,
 ver commonpath().
>>>
>>> os.path.commonprefix(['/usr/lib', '/usr/local/lib'])
'/usr/l'

>>> os.path.commonpath(['/usr/lib', '/usr/local/lib'])
'/usr'
Cambiado en la versión 3.6: Acepta un objeto similar a una ruta .
"""

os.path.dirname( camino ) 
"""Devolver el nombre del directorio de la ruta camino . Este es el primer elemento del par devuelto al pasar la 
ruta a 
la función split().

Cambiado en la versión 3.6: Acepta un objeto similar a una ruta ."""

os.path.exists( camino ) 
"""Devolver Truesi la ruta se refiere a una ruta existente o un descriptor de archivo abierto. Devoluciones 
False por enlaces simbólicos rotos. En algunas plataformas, esta función puede regresar Falsesi no se concede permiso 
para ejecutarse os.stat()en el archivo solicitado, incluso si la ruta existe físicamente.

Cambiado en la versión 3.3: la ruta ahora puede ser un entero: Truese devuelve si es un descriptor de archivo abierto, 
e lo Falsecontrario. """

os.path.lexists( camino ) 
"""Devolver True si la ruta se refiere a una ruta existente. Devoluciones Truepor enlaces simbólicos rotos. 
Equivalente a exists()en plataformas faltantes os.lstat().

Cambiado en la versión 3.6: Acepta un objeto similar a una ruta .

.
.
.
.

"""
