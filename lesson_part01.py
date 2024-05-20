import requests
from bs4 import BeautifulSoup

url = ""

response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

rows = soup.find_all("tr")  # tr - это тэг для ряда в таблице, td - ячейка таблицы

data = []
for row in rows:
    col = row.find_all("td")
    # Удалить лишние пробелы:
    cleaned_cols = [col.text.strip() for col in cols]
    data.append(cleaned_cols)

print(data)

