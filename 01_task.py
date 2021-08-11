import requests
from pprint import pprint

TOKEN = '2619421814940190'

API_BASE_URL = 'https://superheroapi.com/api/2619421814940190'
heroes = {}

for name in ('Hulk', 'Captain America', 'Thanos'):
    response = requests.get(API_BASE_URL + "/search/" + name)
    heroes[name] = response.json()
    # pprint(heroes)


hulk = [heroes['Hulk']['results'][0]['name'],
        heroes['Hulk']['results'][0]['powerstats']['intelligence'],
        # heroes['Hulk']['results'][0]['id']

        ]
# pprint(hulk)
thanos = [heroes['Thanos']['results'][0]['name'],
          heroes['Thanos']['results'][0]['powerstats']['intelligence'],
          # heroes['Thanos']['results'][0]['id'],
        ]
# pprint(thanos)

captain_america = [heroes['Captain America']['results'][0]['name'],
                   heroes['Captain America']['results'][0]['powerstats']['intelligence'],
                   # heroes['Captain America']['results'][0]['id']

        ]
# pprint(captain_america)

all_heroes = [hulk, thanos, captain_america]

smartest = 0

for n in all_heroes:
    # print(n)
    if int(n[1]) > smartest:
        smartest = int(n[1])
        name_hero = n[0]

print(f"Самый умный из трех супер-героев - {name_hero}, потому что у него уровень интеллекта: {smartest}")




