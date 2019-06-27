from flask import Flask
from flask import render_template, request, flash
from flask import redirect, url_for
import models as coneccion
import sqlite3
app =  Flask(__name__)

##Settings
app.secret_key = 'secreto'
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/crear')
def crear_cuenta():
    return render_template('formulario.html')

@app.route('/pelicula')
def pelicula():
    datos = coneccion.consulta_pelicula()
    return render_template('catalogo.html', pel = datos)

@app.route('/config')
def config():
    datos = coneccion.consulta()
    return render_template('tabla.html', contacts = datos)

@app.route('/add', methods =['POST'])
def add_contact():
    if request.method == 'POST':
        usuario_id = request.form['usuario_id']
        ap_pat = request.form['ap_pat']
        ap_mat = request.form['ap_mat']
        direccion = request.form['direccion']
        email = request.form['correo']
        print(usuario_id)
        print(ap_pat)
        print(ap_mat)
        print(direccion)
        print(email)
        try:
            coneccion.insertusers(usuario_id, ap_pat, ap_mat, direccion, email)
            flash('Tu cuenta ha quedado Registrada, por favor inicia sesion')
            return redirect(url_for('index'))
        except sqlite3.IntegrityError:
            flash('Tu cuenta no se pudo registrar, por favor intentalo de nuevo')
            return redirect(url_for('index'))
    else:
        return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)