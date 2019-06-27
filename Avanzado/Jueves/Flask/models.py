import sqlite3 as sql

def insertusers(usuario_id, ap_pat, ap_mat, direccion, correo):
    con = sql.connect("DB/baseFlask.db")
    cursor = con.cursor()
    cursor.execute("INSERT INTO usuario VALUES(?, ?, ?, ?, ?)", (usuario_id, ap_pat, ap_mat, direccion, correo))
    con.commit()
    con.close()

def consulta_usuarios():
    con = sql.connect("DB/baseFlask.db")
    cursor = con.cursor()
    cursor.execute("SELECT * FROM usuario")
    datos = cursor.fetchall()
    print(datos)
    con.commit()
    con.close()
    return datos

def consulta_pelicula():
    con = sql.connect("DB/baseFlask.db")
    cursor = con.cursor()
    cursor.execute("SELECT * FROM pelicula")
    datos = cursor.fetchall()
    print(datos)
    con.commit()
    con.close()
    return datos