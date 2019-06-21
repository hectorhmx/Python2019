# -*- coding: utf-8 -*-
from random import choice,randint,SystemRandom
##Crea un diccionario con los nombres de las victimas y una lista:
#[Correo,Mensajes....]
def cargarVictimas():
    vivas = ["","Ligar asistentes no cuenta como dar clase","Kiero beca xd","Hacerle la barba a gobantes no cuenta como trabajar","Se cancelo Python Avanzado por falta de recursos, por su comprension, gracias","Sin sandwich no hay curso","send changuich","Deja de ligar menores","Deja de ligar prebes","Sin beca no hay curso prebe","no rifas :c","gei el que lo lea"]
    aldo = ["","Aqui esta tu api >:v x2","La neta no rifas :(","Aldo dalto daltonico","Si mando esto en morado si lo veras?","Los editores claros son para putos","Cor.l manda saludos (Mira esa expresion regular)","Te amamos <3","Ahora es personal","Nuestro Daltonico Favorito!!! Mr Dalto!!!","Te amo, pero como amigos"]
    cabello = ["","Y los sandwiches?","No te vas a quedar","Cabellin eres un Pillin con las asintentesillas","Ve a llorar con papi Neto","Eres el mejor hermano prebe :3","No eres el hector chido"]
    oscar = ["","Orale, pelon","Quimica te manda saludos >:v","Aqui esta tu manual de redes","Te amamos chaparro <3","Pm es mejor que AM","Los godines aqui no duran mucho","Sentarse en las piernas de gob's no cuenta como trabajar","Y mi sandwich?"]
    montecillo = ["alejandro.montecillo@gmail.com","Montanita xdxdxdxd","Fakiu","Si ni sabes bases","Tu eres Rodrigo Francisco no?"]
    gueva=["","Eres amante de pato?","Python es mejor que Java","Java esta bien culero :c","Te amamos Gueva <3"]
    victim = {"Vivas":vivas,"AldoRvv":aldo,"Cabello":cabello,"Oscar":oscar,"Montecillo":montecillo,"Gueva":gueva}
    return victim


##Devolvera un becario como victima
def selectBecario(victim):
    becarios = list(victim.keys())
    return choice(becarios)
###Devolvera un el correo a atacar y el mensaje que le llegara
def createMessage(becario,victim):
    correo = victim[becario][0]
    secure_random = SystemRandom() ###Random seguros
    mensaje = secure_random.choice(victim[becario][1:])
    #print(correo,mensaje)
    return ("pythonislove123@gmail.com",mensaje)#(correo,mensaje)###Borrar la linea anterior

def generateHead():
    mensajes = ["PythonPM es mejor que AM","Quiere llorar, quiere llorar","PM no tiene denuncias por acoso","Somos legion, no perdonamos, no olvidamos","PM > AM att Los zetas","PM >> AM","PAITHON PM IS BETTER THAN AM","Que hueva pararse a las 8","Si ni saben programar","Los amamos bai <3","9 de cada 10 asistentes prefieren PM","PM IS BACK BITCHES"]
    return choice(mensajes)+str(randint(1,100))
if __name__ == "__main__":
    victimas = cargarVictimas()
    becario = selectBecario(victimas)
    (correo,mensaje) = createMessage(becario,victimas)
    print(correo,mensaje)
    print(generateHead())
