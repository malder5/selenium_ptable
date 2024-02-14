import time
from selenium.webdriver.common.by import By

from base import Сhemical_element
from selenium import webdriver

final = []
link = 'https://ptable.com'

#TODO Добавить remote режим, чтобы можно было запускать удалённо любые скрипты.
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')

# Запускаем работу
driver = webdriver.Chrome(options=chrome_options)
driver.get(link)

#TODO Добавить динамическое ожидание таблицы.
time.sleep(2)

# Находим элементы
elems = driver.find_elements(By.CSS_SELECTOR, 'li[tabindex="0"]')

# Парсим элементы
for elem in elems:
    him_elem = Сhemical_element()
    him_elem.name = elem.find_element(By.CSS_SELECTOR, 'em').text
    him_elem.atomic = elem.find_element(By.CSS_SELECTOR, 'b').text
    him_elem.weight = elem.find_element(By.CSS_SELECTOR, 'data').text
    final.append(him_elem)

driver.close()

#TODO Упаковать в докер-контейнер

