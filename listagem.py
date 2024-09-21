from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time, collections

driver = webdriver.Chrome()

driver.get("https://www.kabum.com.br/")
wait = WebDriverWait(driver, 10)

fonte = wait.until(EC.presence_of_element_located((By.TAG_NAME, 'input')))
fonte.send_keys('fonte Corsair', Keys.ENTER)
time.sleep(5)

def selecionar_opcao(index):
    select_element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'cUHvqY')))
    select = select_element.find_element(By.CLASS_NAME, 'eGIppJ')
    select.click()
    
    time.sleep(2)
    
    options = select.find_elements(By.TAG_NAME, 'option')
    options[index].click()

def obter_listagem():
    main_class = wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'cWkplc')))
    h3_elements = main_class.find_elements(By.TAG_NAME, 'h3')
    return [h3.text for h3 in h3_elements]

def navegar_pagina(index):
    page_selector = driver.find_element(By.XPATH, '//ul[@class="pagination"]')
    page_number = page_selector.find_elements(By.TAG_NAME, 'li')
    page_number[index].click()
    
    time.sleep(5)

listagem_geral = []

for opcao in [0, 3, 2]: 
    selecionar_opcao(opcao)
    listagem_geral.extend(obter_listagem())

navegar_pagina(2)

for opcao in [0, 3, 2]:  
    selecionar_opcao(opcao)
    listagem_geral.extend(obter_listagem())

navegar_pagina(3)

for opcao in [0, 3, 2]:  
    selecionar_opcao(opcao)
    listagem_geral.extend(obter_listagem())

fonte_counts = collections.Counter(listagem_geral)

top5 = fonte_counts.most_common(5)

print("\n ==As 5 melhores fontes!--\n")
for fonte, count in top5:
    print(f"{fonte}: \n{count} vezes")
print("\n --As 5 melhores fontes!--\n")

time.sleep(10)


driver.quit()
