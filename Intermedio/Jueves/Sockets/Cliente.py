#cliente
import socket
recvIp = input("Ingresa la IP con la que te quieres conectar: ")
s = socket.socket()
##Nos conectamos al servidor con el metodo connect. Tiene 2 aparametros:
#El primero es la IP del servidor
#El segundo parametro es el puerto de conexion
s.connect((recvIp, 9000))
while True:
	mensaje = input("Ingresa el mensaje: ")
	s.send(mensaje.encode())
	if mensaje == "adios":
		break
	respuesta = s.recv(1024).decode()
	print("Respuesta del servidor: ", respuesta)
print("Conexion finalizada")
s.close()