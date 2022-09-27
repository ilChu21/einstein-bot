import json, requests, os
from datetime import datetime


def afCheck(address):
    pigcreditingMethodId = '0x97b0a28a'
    pigLpcreditingMethodId = '0x0a15c37a'
    dogCreditingMethodId = '0xd09f18ce'
    dogBusdCreditingMethodId = '0xabeed456'
    dogWbnbCreditingMethodId = '0x506cd12d'

    afpClaimMethodId = '0x190efe18'
    afdClaimFunctionName = 'claimDogs()'
    afdLpClaimMethodId = '0xac40d739'

    pigOut = {}
    pigLpOut = {}
    dogOut = {}
    dogBusdOut = {}
    dogWbnbOut = {}

    afpIn = {}
    afdIn = {}
    afdLpIn = {}

    transactions = json.loads(requests.get(f'https://api.bscscan.com/api?module=account&action=txlist&address={address}&startblock=0&endblock=99999999&sort=asc&apikey={os.environ["BSCSCAN_TOKEN"]}').text)
    for transaction in transactions['result']:
        if transaction['methodId'] == pigcreditingMethodId and transaction['isError'] == '0':
            date = datetime.utcfromtimestamp(transaction['timeStamp']).strftime('%Y-%m-%d %H:%M:%S')
            hashLink = transaction['hash']
            pigOut[date] = hashLink

        if transaction['methodId'] == pigLpcreditingMethodId and transaction['isError'] == '0':
            date = datetime.utcfromtimestamp(transaction['timeStamp']).strftime('%Y-%m-%d %H:%M:%S')
            hashLink = transaction['hash']
            pigLpOut[date] = hashLink

        if transaction['methodId'] == dogCreditingMethodId and transaction['isError'] == '0':
            date = datetime.utcfromtimestamp(transaction['timeStamp']).strftime('%Y-%m-%d %H:%M:%S')
            hashLink = transaction['hash']
            dogOut[date] = hashLink

        if transaction['methodId'] == dogBusdCreditingMethodId and transaction['isError'] == '0':
            date = datetime.utcfromtimestamp(transaction['timeStamp']).strftime('%Y-%m-%d %H:%M:%S')
            hashLink = transaction['hash']
            dogBusdOut[date] = hashLink

        if transaction['methodId'] == dogWbnbCreditingMethodId and transaction['isError'] == '0':
            date = datetime.utcfromtimestamp(transaction['timeStamp']).strftime('%Y-%m-%d %H:%M:%S')
            hashLink = transaction['hash']
            dogWbnbOut[date] = hashLink

        if transaction['methodId'] == afpClaimMethodId and transaction['isError'] == '0':
            date = datetime.utcfromtimestamp(transaction['timeStamp']).strftime('%Y-%m-%d %H:%M:%S')
            hashLink = transaction['hash']
            afpIn[date] = hashLink

        if transaction['functionName'] == afdClaimFunctionName and transaction['isError'] == '0':
            date = datetime.utcfromtimestamp(transaction['timeStamp']).strftime('%Y-%m-%d %H:%M:%S')
            hashLink = transaction['hash']
            afdIn[date] = hashLink

        if transaction['methodId'] == afdLpClaimMethodId and transaction['isError'] == '0':
            date = datetime.utcfromtimestamp(transaction['timeStamp']).strftime('%Y-%m-%d %H:%M:%S')
            hashLink = transaction['hash']
            afdLpIn[date] = hashLink

    return {'pigOut': pigOut, 'pigLpOut': pigLpOut, 'dogOut': dogOut, 'dogBusdOut': dogBusdOut, 'dogWbnbOut': dogWbnbOut,
            'afpIn': afpIn, 'afdIn': afdIn, 'afdLpIn': afdLpIn,}
