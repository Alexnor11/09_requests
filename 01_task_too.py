import requests
from pprint import pprint
# Второй вариант решения поиск героя по id

API_BASE_URL = 'https://superheroapi.com/api/2619421814940190'

# Узнать id героя:
for name in ('Hulk', 'Captain America', 'Thanos'):
    response = requests.get(API_BASE_URL + "/search/" + name)
    # pprint(response.json())

hulk_id = requests.get(API_BASE_URL + "/332")
hulk = hulk_id.json()
hulk = hulk['name'], hulk['powerstats']['intelligence']
# print(hulk)

c_america_id = requests.get(API_BASE_URL + "/149")
c_america = c_america_id.json()
captain_america = c_america['name'], c_america['powerstats']['intelligence']
# print(captain_america)

thanos_id = requests.get(API_BASE_URL + "/655")
thanos = thanos_id.json()
thanos = thanos['name'], thanos['powerstats']['intelligence']
# print(thanos)

all_heroes = [hulk, thanos, captain_america]

smartest = 0

for n in all_heroes:
    # print(n)
    if int(n[1]) > smartest:
        smartest = int(n[1])
        name_hero = n[0]

print(f"Самый умный из трех супер-героев - {name_hero}, потому что у него уровень интеллекта: {smartest}")