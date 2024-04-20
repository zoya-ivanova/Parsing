import time
import requests
from lxml import html
import csv

# Определяем URL страницы Wikipedia
url = "https://www.imdb.com/chart/moviemeter/?ref_=nv_mv_mpm"
headers = {"User-Agent" : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36 Edg/123.0.0.0'}

# Отправляем HTTP GET-запрос на указанный URL
resp = requests.get(url, headers)
if resp.status_code == 200:
    print("Успешный GET-запрос!")
else:
    print("GET-запрос отклонен с кодом состояния:", resp.status_code)

tree = html.fromstring(html=resp.content)
movies = tree.xpath("//tbody/tr")
all_movies = []

for movie in movies:
    m={
        'name' : movie.xpath(".//td[@class='titleColumn']/a/text()")[0],
        'release_year' : movie.xpath(".//td/span[@class='secondaryInfo']/text()")[0],
        'position' : movie.xpath(".//td/div[@class='velocity']/text()")[0],
        'titlemeter' : movie.xpath(".//span[contains(@class, 'global-sprite titlemeter')]/@class"),
        'position_change' : movie.xpath(".//div/span[@class='secondaryInfo']/text()[2]")}
    
    all_movies.append(m)
    time.sleep(1)

print(all_movies)
print(len(all_movies))