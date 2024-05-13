# Selenium в Python
# Выберите веб-сайт, который позволяет осуществлять скрейпинг (убедитесь в соблюдении условий обслуживания сайта).
# Используя Selenium, напишите сценарий для автоматизации процесса перехода на нужную страницу сайта.
# Определите элементы HTML, содержащие информацию, которую вы хотите извлечь (например, заголовки статей, названия продуктов, цены и т.д.).
# Обработайте любые ошибки или исключения, которые могут возникнуть в процессе скрейпинга.
# Протестируйте свой скрипт на различных сценариях, чтобы убедиться, что он точно извлекает нужные данные.
# Предоставьте ваш Python-скрипт с кратким описанием. 
# Укажите URL сайта, который вы выбрали для анализа. 
# Включите образец извлеченных данных в выбранном вами структурированном формате (например, CSV или JSON). 
# Обязательно соблюдайте условия обслуживания сайта и избегайте чрезмерного скрейпинга, который может нарушить нормальную работу сайта.

from selenium import webdriver  # класс управления браузером
from selenium.webdriver.common.by import By
import time
import csv

# Запуск браузера Chrome
browser = webdriver.Chrome()

# Переход на первую страницу веб-сайта
browser.get("http://quotes.toscrape.com/page/1/")

# Инициализация пустого списка для хранения цитат
quotes = []
while True:
    # Поиск всех цитат на странице с помощью xpath
    quote_elements = browser.find_elements(By.XPATH,'//div[@class="quote"]')
    # Извлечение текста каждой цитаты
    for quote_element in quote_elements:
        quote = quote_element.find_element(By.XPATH,'.//span[@class="text"]').text
        author = quote_element.find_element(By.XPATH,'.//span/small[@class="author"]').text
        quotes.append({"quote": quote, "author": author})
    
    # Проверка наличия следующей кнопки
    next_button = browser.find_elements(By.XPATH,'//li[@class="next"]/a')
    if not next_button:
        break
    
    # Нажатие следующей кнопки
    next_button[0].click()
    
    # Ожидание загрузки страницы
    time.sleep(2)
    
# Закрытие браузера
browser.close()

# Вывод цитат
# for quote in quotes:
#     print(quote["quote"], "by", quote["author"])

# Запись данных в файл CSV
with open("quotes.csv", "w", newline="") as file:
    writer = csv.DictWriter(file, fieldnames=["quote", "author"])
    writer.writeheader()
    writer.writerows(quotes)

# Закрытие браузера
browser.close()
