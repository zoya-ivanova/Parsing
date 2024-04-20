""""Парсинг (HTML. XPath) веб-страницы Worldathletics с табличными данными: 

Топ-лист сезона 2024 по Марафону среди женщин старшей возрастной категории.
Дистанция марафонского бега – это 42 км 195 м, лидер среди всех спортивных дисциплин на выносливость.

Примечание: Пожалуйста, не забывайте соблюдать этические и юридические нормы при веб-скреппинге"""

import time
import requests
from lxml import html
import csv
from datetime import date

# Определяем URL страницы рекордов мирового Марафона среди женщин, прописываем User-Agent
url = "https://worldathletics.org/records/toplists/road-running/marathon/all/women/senior/2024?regionType=world&page=1&bestResultsOnly=true&maxResultsByCountry=all&eventId=10229534&ageCategory=senior"
headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36 Edg/123.0.0.0'}

try:
    # Отправляем GET-запрос на указанный URL
    response = requests.get(url, headers)
    response.raise_for_status()
    print("Успешный GET-запрос!")
except requests.RequestException as e:
    print(f"Ошибка при выполнении GET-запроса: {e}")
    exit()

# Создаем парсинг-дерево lxml из содержимого объекта ответа
tree = html.fromstring(response.content)

# Создаем переменную, где будет список, содержащий все элементы типа tr, из которых нам нужно получить содержимое.
rows = tree.xpath("//table[@class='records-table']/tbody/tr")
data_list = list()
for row in rows:
    row_data = row.xpath(".//td/text()")
    try:
        marathon  = {}
        marathon['Rank'] = int(row_data[0].strip())
        marathon['Mark'] = row_data[1].strip()
        marathon['WIND'] = float(row_data[2].strip() if row_data[2].strip() else 0)
        marathon['Competitor'] = row.xpath(".//td[4]/a/text()")[0].strip()
        marathon['DOB'] = row_data[5].strip()
        marathon['Nat'] = row_data[7].strip()
        marathon['Pos'] = row_data[8].strip()
        marathon['Venue'] = row_data[9].strip()
        marathon['Date'] = row_data[10].strip()
        marathon['ResultScore'] = int(row_data[11].strip())

        data_list.append(marathon)
        time.sleep(1)
    except (ValueError, IndexError) as e:
        print(f"Ошибка при обработке строки: {e}")

# Сохраняем извлеченные данные в CSV-файл 
csv_marathon_womens = f"marathon_records_{date.today()}.csv"
with open(csv_marathon_womens, mode="w", newline="", encoding="utf-8") as csv_file:
    fieldnames = data_list[0].keys()
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(data_list)

print(f"Извлеченные данные сохранены в файле {csv_marathon_womens}")