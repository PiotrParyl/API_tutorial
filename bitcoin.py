import api_key
import requests

headers = {
    'X-CMC_PRO_API_KEY' : api_key.key,
    'Accepts': 'application/json',

}

params = {
    'start' : '1',
    'limit' : '5',
    'convert' : 'USD',
}

url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'

json = requests.get(url, params=params, headers=headers).json()

coins = json['data']

for x in coins:
    print(x['symbol'],x['quote']['USD']['price'])


