import json
from clickhouse_driver import Client

# Подключение к серверу ClickHouse
client = Client('localhost')

# Создание базы данных (если она не существует)
client.execute('CREATE DATABASE IF NOT EXISTS bookstore')

# Создание таблицы 'books'
client.execute('''
CREATE TABLE IF NOT EXISTS bookstore.books (
    id UInt64,
    title String,
    price UInt64,
    available UInt32,
    description String
) ENGINE = MergeTree()
ORDER BY id
''')

# Вывод сообщения о создании таблицы
print("Таблица 'books' создана успешно.")

# Загрузка данных из файла JSON
with open('books.json', 'r') as file:
    data = json.load(file)

# Вставка данных в таблицу
for book in data:
    client.execute("""
    INSERT INTO bookstore.books (id, title, price, available, description)
    VALUES""",
    [(book['id'], book['title'], book['price'], book['available'], book['description'])])

# Вывод сообщения о внесении данных
print("Данные внесены успешно.")