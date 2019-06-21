CREATE TABLE pelicula(
    pelicula_id NUMBER(20) PRIMARY KEY,
    nombre VARCHAR2(40),
    genero VARCHAR2(40),
    anio NUMBER(60))
;
CREATE TABLE director(
    director_id NUMBER(20) PRIMARY KEY,
    nombre VARCHAR2(40),
    apellido_pat VARCHAR2(40),
    apellido_mat VARCHAR2(40),
    fecha_nac DATE,
    pelicula_id NOT NULL CONSTRAINT pelicula_id_fk REFERENCES pelicula(pelicula_id))
;
CREATE TABLE estudiante(
    estudiante_id NUMBER(10) CONSTRAINT estudiante_id_pk PRIMARY KEY,
    nombre VARCHAR2(90) NOT NULL,
    direccion VARCHAR2(90) NOT NULL,
    calificacion NUMBER(10),
    grado_actual VARCHAR2(90) NOT NULL
)
;