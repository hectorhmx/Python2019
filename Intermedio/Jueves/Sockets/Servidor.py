#servidor
import socket
recvIP = input("Ingrese la IP con la cual te quieres Conectar: ")
ss = socket.socket()
##Con el metodo bind se le indica qu epuerto se quiere escuchar
ss.bind((recvIP,9000))
ss.listen(1)
conn, addr = ss.accept()
print("Iniciando el servidor")
print("Cliente conectado desde: ", addr[0], ": ", addr[1])

while True:
	recibido = conn.recv(5000).decode()
	if recibido == "adios":
		break
	print("Client >> ", recibido)
	conn.send(input("Ingresa tu mensaje >> ").encode())
print("Se ha terminado la conexion")
ss.close()#