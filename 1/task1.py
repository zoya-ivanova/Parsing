import json
import requests
import pandas as pd

client_id = "__"
client_secret = "__"

endpoint = "https://api.foursquare.com/v3/places/search"

city = input("Введите город: ")
place = input("Введите заведение: ")
params = {
    "client_id": client_id,
    "client_secret": client_secret,
    "near": city,
    "query": place
}

headers = {
    "Accept": "application/json",
    "Authorization": "fsq3V3AFHzvqod5PVkb9j5ptfec29VfLTGG2XbHrQEGC8bI="
}

response = requests.get(endpoint, params=params, headers=headers)          
if response.status_code == 200:
    # print(response.text)
    data = json.loads(response.text)
    venues = data['results']

    some_list = []
    for ven in venues:
        name = ven['name']
        address = ven.get('location', {}).get('address', 'адрес не указан')    
        geocodes = ven.get('geocodes', {}).get('main', {}).get('latitude', 'не указана'), ven.get('geocodes', {}).get('main', {}).get('longitude', 'не указана')
        some_list.append({'название': name, 'адрес': address, 'координаты': geocodes})

    df = pd.DataFrame(some_list)
else:
    print(response.status_code)

print(df.head(30))

