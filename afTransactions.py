import json, requests, os


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
            pigOut[transaction['hash']] = transaction['timeStamp']

        if transaction['methodId'] == pigLpcreditingMethodId and transaction['isError'] == '0':
            print(transaction['hash'])
            pigLpOut[transaction['hash']] = transaction['timeStamp']

        if transaction['methodId'] == dogCreditingMethodId and transaction['isError'] == '0':
            dogOut[transaction['hash']] = transaction['timeStamp']

        if transaction['methodId'] == dogBusdCreditingMethodId and transaction['isError'] == '0':
            dogBusdOut[transaction['hash']] = transaction['timeStamp']

        if transaction['methodId'] == dogWbnbCreditingMethodId and transaction['isError'] == '0':
            dogWbnbOut[transaction['hash']] = transaction['timeStamp']

        if transaction['methodId'] == afpClaimMethodId and transaction['isError'] == '0':
            afpIn[transaction['hash']] = transaction['timeStamp']

        if transaction['functionName'] == afdClaimFunctionName and transaction['isError'] == '0':
            afdIn[transaction['hash']] = transaction['timeStamp']

        if transaction['methodId'] == afdLpClaimMethodId and transaction['isError'] == '0':
            afdLpIn[transaction['hash']] = transaction['timeStamp']

    return {'pigOut': pigOut, 'pigLpOut': pigLpOut, 'dogOut': dogOut, 'dogBusdOut': dogBusdOut, 'dogWbnbOut': dogWbnbOut,
            'afpIn': afpIn, 'afdIn': afdIn, 'afdLpIn': afdLpIn,}
