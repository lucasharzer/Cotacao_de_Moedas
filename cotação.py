from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep


driver = webdriver.Chrome(executable_path="./chromedriver.exe")

driver.implicitly_wait(3)
sleep(3)

# Entrar no google
driver.get("https://www.google.com.br/")

sleep(10)

driver.maximize_window()

# Buscar a cotação do dólar
driver.find_element_by_xpath(
    '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys("cotação do dólar")

driver.find_element_by_xpath(
    '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys(Keys.ENTER)

dolar = driver.find_element_by_xpath(
    '//*[@id="knowledge-currency__updatable-data-column"]/div[1]/div[2]/span[1]').get_attribute("data-value")

# Buscar a cotação do euro
driver.get("https://www.google.com.br")

driver.find_element_by_xpath(
    '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys("cotação do euro")

driver.find_element_by_xpath(
    '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys(Keys.ENTER)

euro = driver.find_element_by_xpath(
    '//*[@id="knowledge-currency__updatable-data-column"]/div[1]/div[2]/span[1]').get_attribute('data-value')

# Buscar a cotação do ouro
driver.get("https://www.melhorcambio.com/ouro-hoje")

sleep(5)

try:
    driver.find_element_by_xpath(
        '//*[@id="aba_extension"]/table/tbody/tr[3]/td/span').click()
except:
    print("\033[1;31mNão é necessário clicar no botão\033[m")

ouro = driver.find_element_by_xpath(
    '//*[@id="comercial"]').get_attribute('value')

sleep(1)

driver.minimize_window()

sleep(3)

driver.close()

# Finalizar com os resultados
print("\033[1;32m- Resultados:\033[m")
print("\n\033[1;34mValor do Dólar: R${:.2f}\nValor do Euro: R${:.2f}\nValor do Ouro: R${}\033[m".format(float(dolar), float(euro), ouro.replace(',', '.')))
