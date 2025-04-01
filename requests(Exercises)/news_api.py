import requests
import json

url = 'https://newsapi.org/v2/top-headlines'
params = {
    'apiKey': '6a9fdf0c6b9e4f41aa32c92c9aec5a42',
    'category': 'general',
    'language':'en',
    'country':'us'
}

try:
    response = requests.get(url, timeout=15, params=params)
    response.raise_for_status()
except requests.exceptions.HTTPError as e:
    print(e)
except requests.ConnectionError as e:
    print(e)
except requests.Timeout as e:
    print(e)
except requests.JSONDecodeError as e:
    print(e)

data = response.json()
print(json.dumps(data, indent = 4))