from selenium import webdriver
from time import sleep
mydriver = webdriver.Firefox()
try:
    mydriver.get("https://docs.google.com/forms/d/e/1FAIpQLSeoBnLXUBlQXlC_H2gQAlbuO9d6k42oYBdhB3NiH3rXM6Yagw/viewform")
    botones = mydriver.find_elements_by_class_name("freebirdFormviewerViewItemsRadioOptionContainer")##Radio button
    cont = 0
    for i in botones:
        cont+=1
        if i.text == "Si":
            i.click()
            sleep(1)
    texto = mydriver.find_element_by_name("entry.1939522088")###Buscando entrada de texto
    texto.send_keys("Hackeado xdxdxd")
    mydriver.execute_script("document.getElementsByName('entry.1939522088')[0].style.backgroundColor='black';")
    sleep(1)
    mydriver.find_element_by_class_name("quantumWizButtonPaperbuttonContent").click()
    input("Programa terminado")
finally:
    mydriver.close()

