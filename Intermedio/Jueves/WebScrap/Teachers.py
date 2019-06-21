# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException as TE

search = input("Dime el nombre de un profesor: ")
mydriver = webdriver.Firefox()####Instanciamos un webdriver de Firefox
mydriver.get("https://www.misprofesores.com/")#####Obtenemos los datos de la pagina
mydriver.implicitly_wait(5)##esperara 5 segundos
barBus = mydriver.find_element_by_name("q")##Se llama q, es un input text, alias barra de busqueda
barBus.clear()
barBus.send_keys(search) ###buscamos al profe
barBus.send_keys(Keys.RETURN) ###Damos enter
##assert "No hay resultados" not in mydriver.page_source
try:
    container = WebDriverWait(mydriver,10).until(EC.presence_of_element_located((By.ID,"___gcse_0")
    ))###Esperara 10 segundos hasta que se encuentre el el elemento deseado
    resultados = container.find_elements_by_class_name("gs-title") ###Son los Titulos de cada eleemento encontrado, agregamos todos

    chosen = []
    for i in resultados:
        if i.tag_name=="a":
            url = i.get_attribute("data-ctorig")###Obtenemos el atributo donde se encuentra la url
            if "/profesores/" in url and i.text != "": ###Comprobamos que sea un profesor y no tenga contenido vacio
                print(i.text)
                print(url," <- Su url")
                chosen.append(url)
    ##Regresar al usuario lo encontrado
    for i in chosen: ##vemos todos los profesores encontrados en la busqueda inicial, entrando a sus paginas una a una
        mydriver.get(i)
        input("continuar")
except TE:
    print("Se acabo el tiempo de busqueda")
finally:
    mydriver.quit()###Salimos del driver y de firefox