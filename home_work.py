# Попробуйте спарсить данные с сайта divan.ru,
# как в прошлом домашнем задании (можно использовать либо Scrapy, либо selenium),
# но теперь ещё и сохраните информацию в csv файл.

import time
import csv
from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()

url = "https://www.divan.ru/category/svet"

driver.get(url)
time.sleep(5)

results = driver.find_elements(By.CLASS_NAME, 'lsooF')
print(results)

parsed_data = []

for result in results:
    try:
        ''' 
        так брали через scrapy
        'name': svet.css('div.lsooF span::text').get(),
        'price': svet.css('div.pY3d2 span::text').get(),
        'link': svet.css('a').attrib['href']
        '''
        # названия
        title = result.find_element(By.CSS_SELECTOR, 'span[itemprop="name"]').text

        # цены
        price = result.find_element(By.CSS_SELECTOR, 'span.ui-LD-ZU').text

        # ссылки
        link = result.find_element(By.CSS_SELECTOR, 'a.ui-GPFV8').get_attribute('href')


        print(f"{title} {price} {link}")

    except Exception as e:

        exception_name = e.__class__.__name__
        print(f"Ошибка при парсинге. Исключение: {exception_name}")

        continue

    parsed_data.append([title, price, link])

driver.quit()

with open("svet.csv", 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Название', 'Цена', 'Ссылка на товар'])
    writer.writerows(parsed_data)
