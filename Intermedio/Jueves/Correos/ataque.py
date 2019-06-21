# -*- coding: utf-8 -*-
import smtplib
import becarios
user = ""
pwd = ""
smtp = smtplib.SMTP("smtp.gmail.com",587) ###Instanciamos un objeto de tipo SMTP
victimas = dict()
try:
    smtp.ehlo()## extended hello, permite empezar una conversación smtp
    smtp.starttls() ## emoueza conexión tls, no se necesita la instrucción anterior
    smtp.login(user,pwd)
    for i in range(5):
        try:
            victimas = becarios.cargarVictimas()
            becario = becarios.selectBecario(victimas)
            (to,mensaje) = becarios.createMessage(becario,victimas)
            print(to,mensaje)
            subject  = becarios.generateHead()
            header = 'To:' + to + '\n' + 'From: ' + user + '\n' + 'Subject:'+subject+'\n'
            msg = header + mensaje
            fallo = smtp.sendmail(user, to, msg) ##retorna una tupla con lo que falló :'v
            if(len(fallo) == 0):
                pass
            else:
                print(fallo)
                print("algo fallo xdxd si ves esto 5 veces, es algo malo")
        except:
            pass
except smtplib.SMTPRecipientsRefused as smtpRR:
    print("Error,no se envio el correo")
    print("Se nego",smtpRR.recipients)
    print(smtpRR.__doc__)
except smtplib.SMTPConnectError as smtpCE:
    print("Error al contectarse al servidor")
    print(smtpCE.__doc__)
except smtplib.SMTPHeloError as smtpHE:
    print("El servidor rechazó la coneccion")
    print(smtpHE.__doc__)
except smtplib.SMTPAuthenticationError as smtpAE:
    print("Error de autenticacion")
    print("Posiblemente esta mal la combinacion dada")
    print(smtpAE.__doc__)
except LookupError as le:
    print("Si ves esto, es que hector programó mal a las 3 am")
    print(le,)
    print(le.__doc__)
    print(le)
except BaseException as be:
    print(be.__cause__)
    print(be.__doc__)
    print(be)
    print("Error catastrofico")
else:
    print("programa terminado sin errores")
finally:
    smtp.close()
