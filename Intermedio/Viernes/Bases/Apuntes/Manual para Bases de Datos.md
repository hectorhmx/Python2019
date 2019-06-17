# Manual para Bases de Datos

Éste manual tiene como objetivo aprender los conceptos básicos sobre Bases de datos relacionales, se usarán los conceptos relacionados y derivados de las Bases de Datos relacionales, por lo tanto se usará el lenguaje *SQL*, como principal motor.

## Representación



### Modelo Chen o *Entidad - Relación*

Es el modelo conceptual más utilizado para el diseño de bases de datos. Fue introducido por Peter Chen en 1976. El modelo entidad relación está formado por un conjunto de conceptos que permiten describir la realidad mediante un conjunto de representaciones gráficas y lingüísticas.

Se basa en la percepción del mundo real que consiste en un conjunto de objetos básicos llamados *entidades* y de *relaciones* entre estos objetos.

A continuación se detallarán los componentes de éste modelo:

##### Entidad

Es un objeto real o abstracto de interés, sobre el que se recoge información y se representa gráficamente mediante un rectángulo y su nombre aparece en el interior en mayúsculas. Un nombre de entidad sólo puede aparecer una vez en el esquema conceptual. Generalmente se expresa con sustantivos.

![1560734949865](/home/galigaribaldi/.config/Typora/typora-user-images/1560734949865.png)

##### Atributos

Es una propiedad o característica asociada a una determinada entidad o relación y por lo tanto común a todos los ejemplares. La representación grafica es por medio de una elipse etiquetada con letra en minúsculas.

![1560736523996](/home/galigaribaldi/.config/Typora/typora-user-images/1560736523996.png)

###### Tipos de Atributos (Opcional)

En función de las características respecto de la entidad que definen, se distinguen varios tipos de atributos

- **Simples**: No se Subdividen

  ![1560737139265](/home/galigaribaldi/.config/Typora/typora-user-images/1560737139265.png)

- **Compuestos**: Se dividen en otro atributos

  ![1560737167786](/home/galigaribaldi/.config/Typora/typora-user-images/1560737167786.png)

- **Multivalorados:** Tiene un conjunto de valores para una entidad concreta. Se representa con doble elipse.

  ![1560737683348](/home/galigaribaldi/.config/Typora/typora-user-images/1560737683348.png)

- **Derivados:** Cuando un valor puede calcularse u obtenerse a partir de otro. Se representa con una elipse con línea discontinua.

  ![1560737710010](/home/galigaribaldi/.config/Typora/typora-user-images/1560737710010.png)

- **Opcionales:** Son usados cuando es posible desconocer el valor del atributo para cierta entidad o no se tiene un valor aplicable.

  ![1560737749496](/home/galigaribaldi/.config/Typora/typora-user-images/1560737749496.png)

Cabe destacar que esta característica es exclusiva de esta notación.

##### Claves o Llaves

La clave o llave de una entidad es un atributo único e irrepetible, del cual se puede acceder facilmente a través de el.

- **Clave ó llave Primaria: **Es un atributo o conjunto de atributos que identifican en forma única a una entidad. Se representa subrayando el nombre del atributo.

  ![1560750233902](/home/galigaribaldi/.config/Typora/typora-user-images/1560750233902.png)

- **Clave ó llave candidata: ** Es un atributo en una entidad débil que la identifica junto con la clave primaria de la entidad fuerte. Se representa subrayando en forma discontinua el atributo.

  ![1560750291102](/home/galigaribaldi/.config/Typora/typora-user-images/1560750291102.png)

**Nota: **Para casos especiales puede darse el concepto de llave Artificial, la cual se denota con la notación *NombreEntidad_ID*. 

##### Relación

Es una asociación, vinculación o correspondencia entre entidades. Se representa gráficamente con un rombo etiquetado en letras minúsculas. Generalmente representadas por verbos .

![1560735064698](/home/galigaribaldi/.config/Typora/typora-user-images/1560735064698.png)

Ejemplo: Compra es un tipo de relación que vincula las entidades CLIENTE Y PRODUCTO.

![1560735409133](/home/galigaribaldi/.config/Typora/typora-user-images/1560735409133.png)

Una relación esta caracterizada por las siguientes caracteristicas:

- **Nombre: **Debe de tener un nombre que la identifique unívocamente.
- **Grado: **Número de tipos de entidad sobre las que se realiza la asociación. La relación del ejemplo anterior es binaria.
- **Tipo de Correspondencia: **Número máximo de ejemplares de cada tipo de entidad que pueden intervenir en un ejemplar del tipo de relación. A esta propiedad también se le denomina *Cardinalidad*



##### Cardinalidad

Número de ejemplares de una entidad asociadas a otro ejemplar de una entidad o de la misma. Para este punto, existen 3 tipos de cardinalidad.

- (1 : 1) ó (1 a 1) = Relación Uno a Uno, donde a cada entidad A le corresponde una y solo una  entidad B

![1560747620598](/home/galigaribaldi/.config/Typora/typora-user-images/1560747620598.png)

- (1 : M) ó (1 : *) =  Relación Uno a Muchos, donde a la entidad A, le corresponde muchos ejemplares de la entidad B

![1560747575916](/home/galigaribaldi/.config/Typora/typora-user-images/1560747575916.png)

- (M : M) ó (* : *) = Relación Muchos a Muchos, donde muchos ejemplares de la Entidad A se asocian con mcuhos ejemplares de la entidad B.

![1560747541678](/home/galigaribaldi/.config/Typora/typora-user-images/1560747541678.png)

![1560747983673](/home/galigaribaldi/.config/Typora/typora-user-images/1560747983673.png)

![1560748143123](/home/galigaribaldi/.config/Typora/typora-user-images/1560748143123.png)

![1560748186087](/home/galigaribaldi/.config/Typora/typora-user-images/1560748186087.png)

##### Ejemplos Entidad Relación

1. **Entidades Reportaje y Periodista**: Un reportaje puede ser desarrollado en equipos de hasat 4 Periodistas (1 : M). A su vez, un periodista puede participar en el desarrollo de varios reportajes (1 : M). Se debe guardar el porcentaje de participación del periodista en cada reportaje. **Importante:** *Considerar que no todos los periodistas hacen reportajes*

   ![1560749530335](/home/galigaribaldi/.config/Typora/typora-user-images/1560749530335.png) 

2. **Juadores y Tutores: ** Se requiere para un equipo de futbol, almacenar la información de  los jugadores y tutores,de los jugadores nos interesa conocer el nombre, apellido paterno, telefonos, fecha de nacimiento, apellido materno, talla y peso. Y de los tutores nos interesa conocer, el nombre, clave, ciudad o estado, calle, número, colonia, C.P, Apellido paterno, apellido materno y municipio. *Nota:* Un jugador puede tener uno o mas tutores, pero un tutor puede tener uno, muchos o ningún jugador.

   ![1560749956309](/home/galigaribaldi/.config/Typora/typora-user-images/1560749956309.png)

### Modelo Físico 

Llamado También Formato Relacional (Relation Format), Formato IE (International Enginnering Format), Formato de Martín (Martin’s Format), Modelo Pata de gallo (Crow’s foot Format), Formato IDEF1X.

Originalmente desarrollado por “The Computer System Laboratory of the National Institute of Standards and Technology “ en diciembre del 1993.

![1560750867761](/home/galigaribaldi/.config/Typora/typora-user-images/1560750867761.png)

![1560750939274](/home/galigaribaldi/.config/Typora/typora-user-images/1560750939274.png)

![1560750978078](/home/galigaribaldi/.config/Typora/typora-user-images/1560750978078.png)

![1560751038888](/home/galigaribaldi/.config/Typora/typora-user-images/1560751038888.png)

![1560751090515](/home/galigaribaldi/.config/Typora/typora-user-images/1560751090515.png)

##### Ejemplos Modelo Físico

**Nota: ** *Se realizarán los ejemplos resueltos en el modelo E - R*

1. **Entidades Reportaje y Periodista**: Un reportaje puede ser desarrollado en equipos de hasat 4 Periodistas (1 : M). A su vez, un periodista puede participar en el desarrollo de varios reportajes (1 : M). Se debe guardar el porcentaje de participación del periodista en cada reportaje. **Importante:** *Considerar que no todos los periodistas hacen reportajes*

   ![1560751372003](/home/galigaribaldi/.config/Typora/typora-user-images/1560751372003.png)

2. **Juadores y Tutores: ** Se requiere para un equipo de futbol, almacenar la información de  los jugadores y tutores,de los jugadores nos interesa conocer el nombre, apellido paterno, telefonos, fecha de nacimiento, apellido materno, talla y peso. Y de los tutores nos interesa conocer, el nombre, clave, ciudad o estado, calle, número, colonia, C.P, Apellido paterno, apellido materno y municipio. *Nota:* Un jugador puede tener uno o mas tutores, pero un tutor puede tener uno, muchos o ningún jugador.

![1560751426687](/home/galigaribaldi/.config/Typora/typora-user-images/1560751426687.png)

Otra manera de responder el ejemplo anterior, es de la siguiente forma, creando una entidad que solo contenga las llaves de la entidad *Jugador_telefono* y *Tutor*, este forma se crea la entidad *Jugador_Tutor*, la cual tiene una llave compuesta, la cual es la llave de la entidad *Jugador_telefono* y *Tutor*.

![1560751461266](/home/galigaribaldi/.config/Typora/typora-user-images/1560751461266.png)

## SQL (Codificando la Base)

SQL *Structured Query Language*, actualmente Database Language Query, es un lenguaje de base de
datos empleado para:

- Creación y manipulación de las estructuras de una base de datos.
- Administración de los datos
- Ejecución de sentencias complejas diseñadas para transformar los datos almacenados en
  información útil.