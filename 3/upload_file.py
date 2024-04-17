"""Системы управления базами данных MongoDB и Кликхаус в Python
Установите MongoDB на локальной машине, а также зарегистрируйтесь в онлайн-сервисе. 
https://www.mongodb.com/ https://www.mongodb.com/products/compass
Загрузите данные который вы получили на предыдущем уроке путем скрейпинга сайта с 
помощью Buautiful Soup в MongoDB и создайте базу данных и коллекции для их хранения.
Поэкспериментируйте с различными методами запросов.
Зарегистрируйтесь в ClickHouse.
Загрузите данные в ClickHouse и создайте таблицу для их хранения."""

from pymongo import MongoClient
import json

# Подключение к MongoDB
client = MongoClient("mongodb://localhost:27017/")

# Создание базы данных 'bookstore' и коллекции 'books'
db = client['bookstore']
collection = db['books']

# Загрузка данных из файла 'books.json'
with open('books.json') as file:
    file_data = json.load(file)

# Вставка данных в коллекцию
collection.insert_many(file_data)

print("Данные успешно загружены в коллекцию 'books'.")
