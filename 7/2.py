from selenium import webdriver  # класс управления браузером
from selenium.webdriver.chrome.options import Options  # Настройки
from selenium.webdriver.common.by import By  # селекторы
from selenium.webdriver.support.ui import WebDriverWait  # класс для ожидания
from selenium.webdriver.support import expected_conditions as EC
import time
import json


user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"
link = "https://www.youtube.com/@progliveru/videos"
chrome_option = Options()
chrome_option.add_argument(f'{user_agent=}')
driver = webdriver.Chrome(options=chrome_option)
try:
    driver.get(link)
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, 'body')))
    time.sleep(2)
    size_length = driver.execute_script("return document.documentElement.scrollHeight")
    print(f'Первый {size_length=}')
    while True:
        driver.execute_script("window.scrollTo(0, document.documentElement.scrollHeight);")
        time.sleep(2)
        size_new = driver.execute_script("return document.documentElement.scrollHeight")

        if size_new == size_length:
            break
        size_length = size_new
    print(f'Второй {size_length=}')
    value = "//*[@id='video-title-link']"
    video_titles = driver.find_elements(By.XPATH, value)
    video_data = {}
    for i in range(len(video_titles)):
        title = video_titles[i].text
        print(title)
except Exception as er:
    print(f'Произошла ошибка: {er}')
finally:
    driver.quit()