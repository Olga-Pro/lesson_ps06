import time
import csv
from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()

url = "https://tomsk.hh.ru/vacancies/programmist"

driver.get(url)
time.sleep(5)

vacancies = driver.find_elements(By.CLASS_NAME, 'vacancy-card--H8LvOiOGPll0jZvYpxIF')
#print(vacancies)

parsed_data = []

for vacancy in vacancies:
    try:
        # названия вакансий
        title = vacancy.find_element(By.CSS_SELECTOR, 'span.vacancy-name--SYbxrgpHgHedVTkgI_cA').text

        # названия компаний
        company = vacancy.find_element(By.CSS_SELECTOR, 'span.company-info-text--O32pGCRW0YDmp3BHuNOP').text

        # зарплаты
        salary = vacancy.find_element(By.CSS_SELECTOR, 'span.compensation-text--cCPBXayRjn5GuLFWhGTJ').text
                                                        # тэг span
        
        # ссылки
        link = vacancy.find_element(By.CSS_SELECTOR, 'a.bloko-link').get_attribute('href')
                                                    # тэг a
        #print(vacancy)
        #print(f"{title} {company}")
    except Exception as e:

        exception_name = e.__class__.__name__
        print(f"Ошибка при парсинге. Исключение: {exception_name}")
        print(vacancy)
        salary = " "
        continue

    parsed_data.append([title, company, salary, link])

driver.quit()

with open("hh.csv", 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Название вакансии', 'Компания', 'Зарплата', 'Ссылка на вакансию'])
    writer.writerows(parsed_data)


