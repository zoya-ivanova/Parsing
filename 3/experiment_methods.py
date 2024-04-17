"""Поэкспериментируйте с различными методами запросов """

from pymongo import MongoClient

# Подключение к MongoDB
client = MongoClient("mongodb://localhost:27017/")

# Выбор базы данных и коллекции
db = client['bookstore']
collection = db['books']

# 1/ Получение количества документов в коллекции
# book_count = collection.count_documents({})

# print(f"Количество имеющихся книг: {book_count}") 
# 2000


# 2/ Найдем книги с названиями, начинающимися с "А" до "С" (не включая)
# book_a_c = collection.find({"title": {"$gte": "B", "$lt": "C"}})

# for book in book_a_c:
#     print(book['title'])          


# 3/ Вычисление средней стоимости книги
# average_price = collection.aggregate([{"$price": {"_id": None, "avgPrice": {"$avg": "$price"}}}])

# for result in average_price:
#     print(f"Средняя стоимость книги: ${result['avgPrice']:.2f}")


# 4/ Найдем книги, в описании которых есть слово world и love
books_world_and_love = collection.find({"description": {"$regex": "world", "$options": "i", "$regex": "love", "$options": "i"}})

# Вывод названий найденных книг и количества найденных книг
print(f"Количество книг с описанием, содержащим слова 'world' и 'love': {books_world_and_love.count()}")
for book in books_world_and_love:
    print(book['title'])
    
