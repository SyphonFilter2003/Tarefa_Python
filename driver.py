from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep

driver = webdriver.Chrome()

driver.get('https://www.mercadolivre.com.br/')
sleep(2)

try:
    cookies_button = driver.find_element(By.XPATH, "//button[@class='cookie-consent-banner-opt-out__action']")
    cookies_button.click()
    sleep(2)
except:
    pass 

search_box = driver.find_element(By.NAME, 'as_word')
search_box.send_keys('fonte Corsair')
search_box.send_keys(Keys.ENTER)

sleep(3)

dropdown_button = driver.find_element(By.ID, ':R2m55e6:-trigger')
dropdown_button.click()

sleep(1)

try:
    lowest_price_option = driver.find_element(By.XPATH, "//li[@data-key='price_asc']")
    lowest_price_option.click()
except Exception as e:
    print(f"Erro ao selecionar 'Menor preço': {e}")

sleep(10)

driver.close()
