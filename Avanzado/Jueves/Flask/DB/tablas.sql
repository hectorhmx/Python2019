DROP TABLE IF EXISTS usuario
;
DROP TABLE IF EXISTS pelicula
;
DROP TABLE IF EXISTS renta
;
CREATE TABLE usuario(
    usuario_id NUMBER(10) PRIMARY KEY,
    ap_pat VARCHAR2(100),
    ap_mat VARCHAR2(100),
    direccion VARCHAR2(100),
    correo VARCHAR2(100)
)
;

CREATE TABLE pelicula(
    pelicula_id NUMBER PRIMARY KEY,
    nombre VARCHAR2(100),
    trama VARCHAR2(1000),
    anio VARCHAR2(100),
    costo NUMBER(100,3),
    imagen VARCHAR2(100)
)
;
CREATE TABLE renta(
    renta_id NUMBER PRIMARY KEY,
    pelicula_id NOT NULL CONSTRAINT pelicula_id_fk REFERENCES pelicula(pelicula_id),
    usuario_id NOT NULL CONSTRAINT usuario_id_fk REFERENCES usuario(usuario_id)
)
;