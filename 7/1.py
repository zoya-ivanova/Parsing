# Задание 1 https://www.youtube.com/@progliveru/videos
# - Импортируйте необходимые библиотеки: 
# selenium, webdriver, By, WebDriverWait, expected_conditions, time и json.
# - Определите User Agent
# - Запустите веб-драйвер Chrome.
# - Перейдите на страницу канала YouTube.
# - Дождитесь загрузки страницы.
# - Установите время паузы прокрутки и получите текущую высоту страницы.

# - Чтобы установить User Agent 
# chrome_options = Options()
# chrome_options.add_argument(f'user-agent={user_agent}')

# - Используйте метод webdriver.Chrome(), чтобы запустить веб-драйвер Chrome.

# - Используйте метод get() объекта драйвера для перехода на страницу канала YouTube.
# - Используйте объект WebDriverWait, чтобы дождаться загрузки страницы.
# - Используйте метод execute_script("return document.documentElement.scrollHeight")
#  объекта драйвера, чтобы получить текущую высоту страницы.
 
#  Задание 2
# - В цикле прокрутите страницу вниз, чтобы загрузить динамически загружаемые видео.
# - Подождите, пока страница загрузит новые добавленные видео.
# - Рассчитайте новую высоту страницы.
# - Проверьте, совпадает ли новая высота с предыдущей. Если да, значит, все видео загружены, и вы можете выйти из цикла.

# Подсказки:
# - Используйте метод execute_script() для прокрутки страницы вниз.
# - Используйте метод time.sleep(), чтобы приостановить выполнение на указанное время.

# - Найдите все названия видео на странице с помощью XPath.
# - Найдите все элементы метаданных на странице с помощью XPath.
# - Извлеките текст из заголовков видео и метаданных.
# - Создайте словарь для хранения данных.

# Задание 4
# - Извлеките соответствующую информацию (просмотры и время) из метаданных.
# - Создайте словарь для хранения извлеченных данных.
# - Сохраните извлеченные данные в файл JSON.

# Подсказки:
# - Разделите текст из метаданных для извлечения просмотров и временных меток с помощью метода .split.
# - Используйте цикл для заполнения словаря извлеченными данными.
# - Используйте метод json.dump() для сохранения данных в JSON-файл.



# from selenium import webdriver # класс управления браузером
# from selenium.webdriver.chrome.options import Options # Настройки 
# from selenium.webdriver.common.by import By # селекторы
# from selenium.webdriver.support.ui import WebDriverWait # класс для ожидания
# from selenium.webdriver.support import expected_conditions as EC
# import time
# user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"

# link = 'https://www.youtube.com/@progliveru/videos'
# chrome_option = Options()
# chrome_option.add_argument(f"{user_agent=}")
# driver = webdriver.Chrome(options=chrome_option)
# driver.get(link)




from selenium import webdriver  # класс управления браузером
from selenium.webdriver.chrome.options import Options  # Настройки
from selenium.webdriver.common.by import By  # селекторы
from selenium.webdriver.support.ui import WebDriverWait  # класс для ожидания
from selenium.webdriver.support import expected_conditions as EC
import time

user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"
link = "https://www.youtube.com/@progliveru/videos"
chrome_option = Options()
chrome_option.add_argument(f'{user_agent=}')
driver = webdriver.Chrome(options=chrome_option)
driver.get(link)
WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.TAG_NAME, 'body')))
time.sleep(1)
size_length = driver.execute_script("return document.documentElement.scrollHeight")
print(f"Первый {size_length=}")
# driver.quit()

# сверху код должен срабатывать
#  далее добавляем к нему цикл
while True:
    driver.execute_script("window.scrollTo(0, document.documentElement.scrollHeight);")
    time.sleep(1)
    size_new = driver.execute_script("return document.documentElement.scrollHeight")
    
    if size_new == size_length:
        break
    size_length == size_new
print(f"Второй {size_length=}")
driver.quit()

# еще вариант
# page_hieght = driver.execute_script("return document.documentElement.scrollHeight")
#     driver.execute_script("window.scrollTo(0, document.documentElement.scrollHeight);")
#     time.sleep(1)
#     page_hieght_new = driver.execute_script("return document.documentElement.scrollHeight")
#     if page_hieght_new == page_hieght:
#         print(page_hieght_new)
#         break
#     time.sleep(1)