import json, requests, decimal


def bnbPrice():
    bnb = json.loads(requests.get('https://api.coingecko.com/api/v3/simple/price?ids=wbnb&vs_currencies=usd').text)
    curBnbPPrice = bnb['wbnb']['usd']
    return curBnbPPrice