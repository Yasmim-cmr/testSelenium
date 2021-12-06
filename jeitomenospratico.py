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
  
while True:
      try:
        dados = driver.find_element(By.CLASS_NAME, "thumbnail").text
      except:
        break
        print(dados)

