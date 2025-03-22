import requests

username = 'tebogomonamodi08'
res = requests.get(f'https://api.github.com/users/{username}/repos', timeout=9)
res.raise_for_status()

items = res.json()
for i in range(0, len(items)):
    print(f'Name of the Repository:{res.json()[i]["name"]}')
    print(f'Decription: {res.json()[i]["description"]}\n')