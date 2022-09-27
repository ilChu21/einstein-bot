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
            hashLink = f"Tx Link - https://bscscan.com/tx/{transaction['hash']}"
            pigOut[f"Date - {date}"] = hashLink

        if transaction['methodId'] == pigLpcreditingMethodId and transaction['isError'] == '0':
            date = datetime.utcfromtimestamp(transaction['timeStamp']).strftime('%Y-%m-%d %H:%M:%S')
            hashLink = f"Tx Link - https://bscscan.com/tx/{transaction['hash']}"
            pigLpOut[f"Date - {date}"] = hashLink

        if transaction['methodId'] == dogCreditingMethodId and transaction['isError'] == '0':
            date = datetime.utcfromtimestamp(transaction['timeStamp']).strftime('%Y-%m-%d %H:%M:%S')
            hashLink = f"Tx Link - https://bscscan.com/tx/{transaction['hash']}"
            dogOut[f"Date - {date}"] = hashLink

        if transaction['methodId'] == dogBusdCreditingMethodId and transaction['isError'] == '0':
            date = datetime.utcfromtimestamp(transaction['timeStamp']).strftime('%Y-%m-%d %H:%M:%S')
            hashLink = f"Tx Link - https://bscscan.com/tx/{transaction['hash']}"
            dogBusdOut[f"Date - {date}"] = hashLink

        if transaction['methodId'] == dogWbnbCreditingMethodId and transaction['isError'] == '0':
            date = datetime.utcfromtimestamp(transaction['timeStamp']).strftime('%Y-%m-%d %H:%M:%S')
            hashLink = f"Tx Link - https://bscscan.com/tx/{transaction['hash']}"
            dogWbnbOut[f"Date - {date}"] = hashLink

        if transaction['methodId'] == afpClaimMethodId and transaction['isError'] == '0':
            date = datetime.utcfromtimestamp(transaction['timeStamp']).strftime('%Y-%m-%d %H:%M:%S')
            hashLink = f"Tx Link - https://bscscan.com/tx/{transaction['hash']}"
            afpIn[f"Date - {date}"] = hashLink

        if transaction['functionName'] == afdClaimFunctionName and transaction['isError'] == '0':
            date = datetime.utcfromtimestamp(transaction['timeStamp']).strftime('%Y-%m-%d %H:%M:%S')
            hashLink = f"Tx Link - https://bscscan.com/tx/{transaction['hash']}"
            afdIn[f"Date - {date}"] = hashLink

        if transaction['methodId'] == afdLpClaimMethodId and transaction['isError'] == '0':
            date = datetime.utcfromtimestamp(transaction['timeStamp']).strftime('%Y-%m-%d %H:%M:%S')
            hashLink = f"Tx Link - https://bscscan.com/tx/{transaction['hash']}"
            afdLpIn[f"Date - {date}"] = hashLink

    return {'pigOut': pigOut, 'pigLpOut': pigLpOut, 'dogOut': dogOut, 'dogBusdOut': dogBusdOut, 'dogWbnbOut': dogWbnbOut,
            'afpIn': afpIn, 'afdIn': afdIn, 'afdLpIn': afdLpIn,}
