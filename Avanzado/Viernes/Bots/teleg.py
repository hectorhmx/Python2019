import telebot ##pip install pyTelegramBotAPI
import os
##Token unico para cada chat
bot = telebot.TeleBot("853305217:AAHSNAmds4v48F1ZIYiyFK2AM1UbvFQhVzo")

@bot.message_handler(commands = ["start", "help"])
def send_welcome(message): ###Message es el mensaje que nos llega como parametro
    print(message)
    chatId = message.chat.id
    usuarionombre = message.chat.first_name + " " + message.chat.last_name
    bot.reply_to(message, "Hola mundo!")
    saludo  ="Hola!! {nombre}, Bienvenido a nuestro Bot"
    bot.send_message(chatId, saludo.format(nombre=usuarionombre))
    

@bot.message_handler(commands = ["Imagen", "imagen"])
def send_imagen(message):
	chatId = message.chat.id
	ruta ="/home/galigaribaldi/Documentos/Semestral/Python2019/Python2019/Avanzado/Viernes/Bots/"
	ruta = ruta + "IT.jpg"
	if not os.path.isfile(ruta):
		print(type(ruta))
		bot.send_message(chatId,text = "Esto no es una imagen")
		bot.send_message(chatId,ruta)
	else:
		f = open(ruta, 'rb')
		bot.send_photo(chatId,f)
		bot.send_message(chatId, text ="Mensaje enviado")
	

@bot.message_handler(func = lambda message: True)
def echo_all(message):
    chatId = message.chat.id
    bot.send_message(chatId, "Cualquier otro mensaje")

print("Its a live.!!")
bot.polling() ##start bot