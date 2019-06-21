import smtplib
 
to = ""
gmail_user = ""
gmail_pwd = ""
smtpserver = smtplib.SMTP("smtp.gmail.com",587)
#smtpserver.ehlo()## extended hello, permite empezar una conversación smtp
smtpserver.starttls() ## emoueza conexión tls, no se necesita la instrucción anterior
smtpserver.login(gmail_user, gmail_pwd)
header = 'To:' + to + '\n' + 'From: ' + gmail_user + '\n' + 'Subject:Pruebas smtp \n'
print(header)
msg = header + '\n Que honda como estas?\n'
print(smtpserver.sendmail(gmail_user, to, msg)) ##retorna una tupla con lo que falló :'v
print ('hecho')
smtpserver.close()
