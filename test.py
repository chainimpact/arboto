import requests

payload = {'market': 'ETHEUR', 'type': 'sell', 'page': 0}

r = requests.get("https://api.cryptomkt.com/v1/book", params=payload)

print(r.json()) 