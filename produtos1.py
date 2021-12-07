from selenium import webdriver

driver = webdriver.Chrome(executable_path=r"C:\WebDriver\bin\chromedriver.exe")
import requests
driver.get("https://webscraper.io/test-sites/e-commerce/allinone/computers/laptops")

driver.implicitly_wait(3) # seconds
import json
listaLinks = []


lista = []

for produtoAtual in driver.find_elements_by_class_name("thumbnail"):
        link = produtoAtual.find_element_by_tag_name("a")
        listaLinks.append(link.get_attribute("href"))

for linkAtual in listaLinks:
        driver.get(linkAtual)
        driver.implicitly_wait(3) # seconds

        nomeProduto = driver.find_element_by_class_name("caption").find_element_by_class_name("description").text
        if("Lenovo" in nomeProduto): 
            precoP = driver.find_element_by_class_name("caption").find_element_by_tag_name("h4").text
            reviews = driver.find_element_by_class_name("ratings").find_element_by_tag_name("p").text
        # preco = driver.find_element_by_id("caption").find_element_by_tag_name("").text
        # try:
        #     avaliacao = driver.find_element_by_class_name("gbStarGrade_count").text
        # except:
        #     avaliacao = "Sem avaliação"
       

            lista.append(('nome do produto: ' + nomeProduto + ' ') + ('preço: ' + precoP + ' ') + 'Reviews: ' + reviews)
      
            
            print(lista)