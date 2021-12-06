from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import presence_of_element_located

#This example requires Selenium WebDriver 3.13 or newer
listaLaptop = []
with webdriver.Chrome() as driver:
    wait = WebDriverWait(driver, 10)
    driver.get("https://webscraper.io/test-sites/e-commerce/allinone/computers/laptops")
    dados = driver.find_element(By.XPATH, "/html/body/div[1]/div[3]/div/div[2]/div/div[31]/div").text

    for laptopAtual in driver.find_element_by_class_name("thumbnail"):
        link = laptopAtual.find_element_by_tag_name("a")
        listaLaptop.append(link.get_attribute("tile"))
    
    for laptopAtual in listaLaptop:
        driver.get(laptopAtual)
        driver.implicitly_await(3)
        nome = driver.find_element_by_class_name("title").text
        preco = driver.find_element_by_class_name("caption").find_element_by_tag_name("h4")


print(nome)
print(preco)