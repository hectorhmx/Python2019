from flask import Flask
from flask import request, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ayuda')
def ayuda():
    return render_template('ayuda.html')

@app.route('/peliculas')
def peliculas():
    return render_template('pelicula.html')


if __name__ == '__main__':
    app.run(debug = True)