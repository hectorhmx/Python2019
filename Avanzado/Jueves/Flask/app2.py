from flask import Flask
from flask import request

app = Flask(__name__)

@app.route("/")
def hola_mundo(nombre="invitado"):
	nombre = request.args.get('nombre', nombre)
	return "Hola {}".format(nombre)

###Funcion que suma desde la url
@app.route("/suma/<num1>/<num2>")
def suma(num1 = 0, num2 = 0):
	num1 = request.args.get('num1', num1)
	num2 = request.args.get('num2', num2)
	return "{} mas {} es igual a {}".format(num1, num2, int(num1)+int(num2))

###host/suma?num1=1&num2=3
@app.route("/suma2")
def suma2(num1 = 0, num2 = 0):
	num1 = request.args.get('num1', num1)
	num2 = request.args.get('num2', num2)
	return "{} mas {} es igual a {}".format(num1, num2, int(num1)+int(num2))

if __name__ == "__main__":
	app.run(debug=True)