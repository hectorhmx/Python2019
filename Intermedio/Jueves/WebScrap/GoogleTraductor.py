from selenium import webdriver
mydriver = webdriver.Firefox()
###Creamos una instancia de un webdriver de firefox
#Collecting accessible data and/or processed output from the application
#Web scrapping -> Obtener información accesible o salidas procesadas de una applicación
try:
    mydriver.get("https://translate.google.com/")
    ###Metodo get, navegara hasta la pagina
    #  esperara a que la pagina haya terminado (envento onload) (cuidado con ajax)

    areaTexto = mydriver.find_element_by_id("source")
    #tendremos un objeto que será el area de 
    print(dir(areaTexto))#ver que tiene el objeto
    areaTexto.send_keys("hello")
    input("end")
    
    
    ##Parte 2
    words = ["dog","hello","I love programming","Sleep is for the weak"]
    for i in words:
        areaTexto.clear()##limpear area de texto
        areaTexto.send_keys(i)
        input("continuar")

    ### Parte 3
    botonInt = mydriver.find_element_by_class_name("swap-wrap")
    print(dir(botonInt))
    botonInt.click()
    palabras = ["hola","Puedo escribir los versos mas tristes esta noche","Solo se que no se nada, pero al menos yo se eso"]
    for i in palabras:
        areaTexto.clear()##limpear area de texto
        areaTexto.send_keys(i)
        input("continuar")
    mydriver.get("https://www.youtube.com/watch?v=aJkXBuhVqYs")
    input("Regresar")
    mydriver.back()##regresar una posicion
    input("volver")
    mydriver.forward()
finally:
    mydriver.close()

