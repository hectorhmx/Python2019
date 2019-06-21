"""
Estos scripts realizan tareas como procesar archivos en un directorio, iniciar programas de prueba, etc. Históricamente, dichos programas se han escrito en lenguajes shell no portables y sintácticamente oscuros. Sin embargo, incluso en 
este dominio relativamente simple, algunos de los mejores atributos de Python brillan intensamente. Por ejemplo, 
la facilidad de uso de Python y la extensa biblioteca incorporada hacen que sea sencillo (e incluso divertido) el uso
de herramientas avanzadas del sistema, como hilos, señales, bifurcaciones, zócalos y sus familiares; estas herramientas 
son mucho menos accesibles bajo la oscura sintaxis de los lenguajes de shell y los lentos ciclos de desarrollo de los 
lenguajes compilados. El soporte de Python para conceptos como claridad de código y OOP también nos ayuda a escribir
herramientas de shell que se pueden leer y reutilizar. Al usar Python, no es necesario comenzar cada nuevo script desde
cero. Además, encontraremos que Python no solo incluye todas las interfaces que necesitamos para escribir herramientas
del sistema, sino que también fomenta la portabilidad de scripts. Al emplear la biblioteca estándar de Python, 
la mayoría de los scripts del sistema escritos en Python se pueden transportar automáticamente a todas las 
plataformas principales. Por ejemplo, normalmente puede ejecutar en Linux un script de procesamiento de 
directorios Python escrito en Windows sin cambiar su código fuente, simplemente copie el código fuente. 
Aunque escribir scripts que logren tal utopía de portabilidad requiere un poco de esfuerzo y práctica 
adicionales, si se usa bien, Python podría ser la única herramienta de scripting del sistema que necesita usar.
"""

import sys,os # importamos los módulos sys y os
#len(dir(sys)) #Nos permite conocer el número de atributos presentes en este módulo en Windows, son más en Unix
#91 
#len(dir(os))#Nos permite conocer el número de atributis presentes en este módulo en Windows, son más en Unix
#150
# El contenido de estos dos módulos puede variar según la versión y plataforma de Python. Por ejemplo, el sistema
# operativo es mucho más grande en Cygwin después de construir Python 3.1 a partir de su código fuente (Cygwin es un 
# sistema que proporciona una funcionalidad similar a Unix en Windows; 

"""
Módulos del sistema Python

 La mayoría de las interfaces de nivel de sistema en Python se envían en solo dos módulos: sys y os.
 Eso es un poco simplificado; Otros módulos estándar pertenecen a este dominio también. Entre ellos se 
 encuentran los siguientes:

* glob para expansión de nombre de archivo
* socket -para conexiones de red y comunicación entre procesos (IPC)
* subprocesos, subprocesos, cola Para ejecutar y sincronizar subprocesos simultáneos
* time, timeit Para acceder a los detalles de la hora del sistema.
* Subproceso, multiprocesamiento para lanzar y controlar procesos paralelos.
* señal, selección, shutil, archivo temporal, y otros Para otras tareas relacionadas con el sistema

Extensiones de terceros, como pySerial (una interfaz de puerto serie), Pexpect (un trabajo de espera similar 
para controlar diálogos entre programas) e incluso Twisted (un marco de trabajo en red) posiblemente también 
pueden agruparse en el dominio de los sistemas. 

Pero en general, sys y os forman el núcleo del arsenal de herramientas del sistema incorporado de Python. 
En principio, al menos, sys exporta componentes relacionados con el propio intérprete de Python (por ejemplo, 
la ruta de búsqueda del módulo), y os contiene variables y funciones que se asignan al sistema operativo en el que 
se ejecuta Python. 
"""

#dir(sys) #Herramientas que nos ofrece el módulo sys, 
#La función dir simplemente devuelve una lista que contiene los 
#nombres de cadena de todos los atributos en cualquier objeto con atributos;
"""
['__breakpointhook__', '__displayhook__', '__doc__', '__excepthook__', '__interactivehook__', '__loader__', '__name__',
__package__', '__spec__', '__stderr__', '__stdin__', '__stdout__', '_clear_type_cache', '_current_frames', 
'_debugmallocstats', '_enablelegacywindowsfsencoding', '_framework', '_getframe', '_git', '_home', '_xoptions',
'api_version', 'argv', 'base_exec_prefix', 'base_prefix', 'breakpointhook', 'builtin_module_names', 'byteorder',
'call_tracing', 'callstats', 'copyright', 'displayhook', 'dllhandle', 'dont_write_bytecode', 'exc_info', 'excepthook',
exec_prefix', 'executable', 'exit', 'flags', 'float_info', 'float_repr_style', 'get_asyncgen_hooks', 
'get_coroutine_origin_tracking_depth', 'get_coroutine_wrapper', 'getallocatedblocks', 'getcheckinterval', 
'getdefaultencoding', 'getfilesystemencodeerrors', 'getfilesystemencoding', 'getprofile', 'getrecursionlimit', 
'getrefcount', 'getsizeof', 'getswitchinterval', 'gettrace', 'getwindowsversion', 'hash_info', 'hexversion', 
'implementation', 'int_info', 'intern', 'is_finalizing', 'last_traceback', 'last_type', 'last_value', 'maxsize', 
'maxunicode', 'meta_path', 'modules', 'path', 'path_hooks', 'path_importer_cache', 'platform', 'prefix', 
'set_asyncgen_hooks', 'set_coroutine_origin_tracking_depth', 'set_coroutine_wrapper', 'setcheckinterval', 
'setprofile', 'setrecursionlimit', 'setswitchinterval', 'settrace', 'stderr', 'stdin', 'stdout', 'thread_info', 
'version', 'version_info', 'warnoptions', 'winver']
"""
#sys.__doc__ #El atributo incorporado __doc__ que se muestra por lo general contiene una cadena de documentación, pero puede parecer un poco extraño 
#PAra hacer esto humanamente legible se imprime con la función print()
#print(sys.__doc__) 
"""
Este módulo proporciona acceso a algunos objetos utilizados o mantenidos por el
intérprete y funciones que interactúan fuertemente con el intérprete.
"""
#En algunas ocasiones puede ser difícil de manejar, por lo que se puede utilizar:
#help(sys) 

#Explorando un poco en nuestra computadora
#sys.platform #Por ejemplo, sus atributos nos dan el nombre del sistema operativo subyacente en el que se ejecuta el código de la plataforma

###Ejemplo de sys.platform
import sys # importamos el módulo sys
if sys.platform[:3] == 'win': #lo que arroja sys.platform es una catena, por lo que podemos partirla en porciones y compararla
#En esta línea la comparamos con "win", es decir, si es windows, hará lo siguiente:
	print('Hola, terrícola, usas Windows') #Imprimir en pantalla este mensaje
if sys.platform[:6] == 'darwin': # Si por el contrario, sys.platform contiene "darwin", significa que es una Mac la que corre el código
	print('Hola, terrícola millonario, usas Mac') #Por lo que imprimirá en pantalla que se trata de este S.O.
if sys.platform[:5] == 'linix': #Por otro lado, si es linux lo que arroja, imprimirá en pantalla otro mensaje	
	print('Hola, terrícola, usas Linux :0')

#sys.path 

"""
El módulo sys también nos permite inspeccionar la ruta de búsqueda del módulo tanto de forma interactiva como 
dentro de un programa Python. sys.path es una lista de cadenas de nombres de directorios que representan la ruta de
búsqueda verdadera en un intérprete de Python en ejecución. Cuando se importa un módulo, Python escanea esta lista 
de izquierda a derecha, buscando el archivo del módulo en cada directorio nombrado en la lista. Debido a eso, este 
es el lugar para verificar que su ruta de búsqueda esté realmente configurada como se esperaba
"""
sys.modules #es un diccionario que contiene un nombre: entrada de módulo para cada módulo importado en su sesión o programa de Python
#Para mostrar las llaves de este diccionario es:
sys.modules.keys()
#Para buscar una llave en específico en el diccionario de sys.modules
'math' in sys.modules 
#y la consola responderá True o False

sys.argv 
"""
Si queremos que nuestra aplicación acepte parámetros tal como lo hace cualquier otra aplicación del sistema
 (ej: cd directorio, la aplicación es "cd" y el argumento es "directorio"), lo podemos hacer en Python con el 
 atributo argv del objeto sys.

El atributo sys.argv es una lista que almacenan los parámetros introducidos.
 Por ejemplo, vamos a hacer un programa que reciba una cadena por parámetro y diga cuantos caracteres tiene

 sys.argv[0] es el nombre del script
 sys.argv[1] es el  primer argumento
 sys.argv[2] es el segundo argumento
 len(sys.argv) da la cantidad de argumentos que se recibieron
 len(sys.argv[1]) es la longitud del primer argumento que se recibió, sinconsiderar el nombre del script
 len(sys.argv[2]) es la longitud del segundo argumento que se recibió, sin considerar el nombre del script 


import sys #improtamos el módulo sys
print ("Este es el nombre del script: " , sys.argv[0]) #Da el nombre del script, el cual es el primer argumento, está en la posición 0 de la lista
print ("Número de argumentos que recibí: " , len(sys.argv)) # da el tamaño de la lista, contanto como argumento 1 el nombre del script
print('La cadena que recibí fue:', sys.argv[1]) # muestra el argumento ingresado, ubicado en 1
print('La longitud de la cadena es: ',len(sys.argv[1])) # muestra la longitud del argumento ingresado
print ("Los argumentos son: " , str(sys.argv)) # contierve a cadena los elementos de la lista y los muestra en pantalla

# La manera de colocar los argumentos es al momento de correrlo, es decir, si mi script o documento se llama "sys.py" 
#y queremos que reciba un argumento:
# python3 sys.py argumento1 
#Si queremos que reciba 2 argumentos:
# python3 sys.py argumento1 argumento2
# etc

#Si deseas conocer más herramientas de Sys y Os, entra en la documentación en : https://www.python.org/doc/
# y explora dir(sys) y dir(os)

import sys #improtamos el módulo sys
print ("Este es el nombre del script: " , sys.argv[0]) #Da el nombre del script, el cual es el primer argumento, está en la posición 0 de la lista
print ("Número de argumentos que recibí: " , len(sys.argv)) # da el tamaño de la lista, contanto como argumento 1 el nombre del script
# print('La cadena que recibí fue:', sys.argv[1]) # muestra el argumento ingresado, ubicado en 1
# print('La longitud de la cadena es: ',len(sys.argv[1])) # muestra la longitud del argumento ingresado
print ("Los argumentos son: " , str(sys.argv)) # contierve a cadena los elementos de la lista y los muestra en pantalla

"""
#¿Qué más se puede hacer con los argumentos? Todo lo que te imagines!!!
# hagamos un pequeño programa que haga operaciones con los argumentos recibidos
# si los argumentos son más de uno (título) y menor a 3, realiza una multiplicación
"""
if len(sys.argv)>1 and len(sys.argv)<=3:
	print('La multiplicación de los argumentos que proporcionaste es: ',int(sys.argv[1])* int(sys.argv[2]))
# si los argumentos son más de 4 (3 argumentos además del título) y menos o igual a 5, realiza una suma de los argumentos proporcionados
if len(sys.argv)>4 and len(sys.argv)<=5:
	print('La suma de los argumentos que proporcionaste es: ',int(sys.argv[1])+int(sys.argv[2])+int(sys.argv[3])+ int(sys.argv[4]))
"""

