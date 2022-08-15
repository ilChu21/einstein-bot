import json, requests, decimal


def bnbPrice():
    bnb = json.loads(requests.get('https://api.coingecko.com/api/v3/simple/price?ids=wbnb&vs_currencies=usd').text)
    curBnbPPrice = bnb['wbnb']['usd']
    return curBnbPPrice


def dripDEXPrice():
    dripDEXPrices = json.loads(requests.get('https://api.drip.community/prices/').text)
    curDripDEXPrice = format(dripDEXPrices[-1]['value'], '.2f')
    return curDripDEXPrice


def dripPCSPrice():
    dripPCSPrices = json.loads(requests.get('https://api.pancakeswap.info/api/v2/tokens/0x20f663cea80face82acdfa3aae6862d246ce0333').text)
    curDripPCSPrice = decimal.Decimal(dripPCSPrices['data']['price'])
    curDripPCSPrice = format(curDripPCSPrice, '.2f')
    return curDripPCSPrice


def br34pPrice():
    br34p = json.loads(requests.get('https://api.coinpaprika.com/v1/tickers/br34p-br34p/').text)
    curBr34pPrice = round(br34p['quotes']['USD']['price'], 2)
    return curBr34pPrice


def afpPCSPrice():
    afpPCSPrices = json.loads(requests.get('https://api.pancakeswap.info/api/v2/tokens/0x9a3321E1aCD3B9F6debEE5e042dD2411A1742002').text)
    curAfpPCSPrice = decimal.Decimal(afpPCSPrices['data']['price'])
    curAfpPCSPrice = format(curAfpPCSPrice, '.2f')
    return curAfpPCSPrice


def dogPCSPrice():
    dogPCSPrices = json.loads(requests.get('https://api.pancakeswap.info/api/v2/tokens/0xDBdC73B95cC0D5e7E99dC95523045Fc8d075Fb9e').text)
    curDogPCSPrice = decimal.Decimal(dogPCSPrices['data']['price'])
    curDogPCSPrice = format(curDogPCSPrice, '.2f')
    return curDogPCSPrice


def oozeApiPrice():
    oozePrices = json.loads(requests.get('https://api.ooze.finance/ooze/price').text)
    curOozePrice = format(oozePrices[-1]['value'])
    return curOozePrice