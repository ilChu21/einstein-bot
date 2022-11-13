import json, requests, decimal


def bnbPrice():
    bnb = json.loads(requests.get('https://api.coingecko.com/api/v3/simple/price?ids=wbnb&vs_currencies=usd').text)
    curBnbPPrice = bnb['wbnb']['usd']
    return curBnbPPrice

# Functions Not In Use
def busdPriceNIU():
    busdPrices = json.loads(requests.get('https://api.pancakeswap.info/api/v2/tokens/0xe9e7cea3dedca5984780bafc599bd69add087d56').text)
    curBusdPrice = decimal.Decimal(busdPrices['data']['price'])
    curBusdPrice = format(curBusdPrice, '.2f')
    return curBusdPrice


def dripDEXPriceNIU():
    dripDEXPrices = json.loads(requests.get('https://api.drip.community/prices/').text)
    curDripDEXPrice = format(dripDEXPrices[-1]['value'], '.2f')
    return curDripDEXPrice


def dripPCSPriceNIU():
    dripPCSPrices = json.loads(requests.get('https://api.pancakeswap.info/api/v2/tokens/0x20f663cea80face82acdfa3aae6862d246ce0333').text)
    curDripPCSPrice = decimal.Decimal(dripPCSPrices['data']['price'])
    curDripPCSPrice = format(curDripPCSPrice, '.2f')
    return curDripPCSPrice


def br34pPriceNIU():
    br34p = json.loads(requests.get('https://api.coinpaprika.com/v1/tickers/br34p-br34p/').text)
    curBr34pPrice = round(br34p['quotes']['USD']['price'], 2)
    return curBr34pPrice


def afpPCSPriceNIU():
    afpPCSPrices = json.loads(requests.get('https://api.pancakeswap.info/api/v2/tokens/0x9a3321E1aCD3B9F6debEE5e042dD2411A1742002').text)
    curAfpPCSPrice = decimal.Decimal(afpPCSPrices['data']['price'])
    curAfpPCSPrice = format(curAfpPCSPrice, '.2f')
    return curAfpPCSPrice


def afdPCSPriceNIU():
    afdPCSPrices = json.loads(requests.get('https://api.pancakeswap.info/api/v2/tokens/0x198271b868daE875bFea6e6E4045cDdA5d6B9829').text)
    curAfdPCSPrice = decimal.Decimal(afdPCSPrices['data']['price'])
    curAfdPCSPrice = format(curAfdPCSPrice, '.2f')
    return curAfdPCSPrice