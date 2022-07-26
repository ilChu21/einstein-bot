import json, requests



def oozePrice():
    oozePrices = json.loads(requests.get('https://api.ooze.finance/ooze/price').text)
    curOozePrice = format(oozePrices[-1]['value'])
    return curOozePrice