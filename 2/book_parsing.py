# Парсинг HTML. 
# BeautifulSoup
# Выполнить скрейпинг данных в веб-сайта http://books.toscrape.com/ и извлечь информацию о всех книгах на сайте во всех категориях: 
# название, цену, количество товара в наличии (In stock (19 available)) в формате integer, описание.
# Затем сохранить эту информацию в JSON-файле.

import requests                # Используется для отправки HTTP-запросов
from bs4 import BeautifulSoup  # Для парсинга HTML и XML документов
import urllib.parse            # Для склейки URL
import re                      # Для работы с регулярными выражениями
import json                    # Для работы с форматом данных JSON
import time                    # Для работы со временем

url = "https://books.toscrape.com/"
books_info = list()
while True:
    website = requests.get(url)                               # Отправка запроса
    html = website.content
    init_soup = BeautifulSoup(html, "html.parser")            # Разбор HTML
    image_containers = init_soup.find_all('div', ('class', 'image_container'))
    rel_links = [container.find('a').get('href') for container in image_containers]
    abs_links = [urllib.parse.urljoin(url, rel_link) for rel_link in rel_links]
    for abs_link in abs_links:
        soup = BeautifulSoup(requests.get(abs_link).content, 'html.parser')
        div = soup.find('div', ('class', 'col-sm-6 product_main'))
        title = div.find('h1').text
        price_str = div.find('p', ('class', 'price_color')).text
        available = div.find('p', ('class', 'instock availability')).text
        available = int(re.findall(r'\b\d+\b', available)[0])
        description = soup.find("meta", attrs={"name": "description"})["content"].strip()
        books_info.append({"title": title, "price": price_str, "available": available, "description": description})
    time.sleep(3)
    next_li = init_soup.find('li', ('class', 'next'))
    if not next_li:
        break
    time.sleep(1)
    next_link = next_li.find('a')['href']
    url = urllib.parse.urljoin(url, next_link)
with open("books.json", "w") as file:      # Открытие файла для записи
    json.dump(books_info, file, indent=4)  # Сохранение данных в формате JSON с отступами



# if __name__ == "__main__":
#     main()