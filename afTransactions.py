import json, requests, os
from datetime import datetime
from web3 import Web3

bsc = "https://bsc-dataseed.binance.org/"
web3 = Web3(Web3.HTTPProvider(bsc))


def afCheck(address):
    address = web3.toChecksumAddress(address)
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
            txDate = datetime.utcfromtimestamp(int(transaction['timeStamp'])).strftime('%Y-%m-%d %H:%M:%S')
            hashLink = f"Tx Link - https://bscscan.com/tx/{transaction['hash']}"
            pigOut[hashLink] = txDate

        if transaction['methodId'] == pigLpcreditingMethodId and transaction['isError'] == '0':
            txDate = datetime.utcfromtimestamp(int(transaction['timeStamp'])).strftime('%Y-%m-%d %H:%M:%S')
            hashLink = f"Tx Link - https://bscscan.com/tx/{transaction['hash']}"
            pigLpOut[hashLink] = txDate

        if transaction['methodId'] == dogCreditingMethodId and transaction['isError'] == '0':
            txDate = datetime.utcfromtimestamp(int(transaction['timeStamp'])).strftime('%Y-%m-%d %H:%M:%S')
            hashLink = f"Tx Link - https://bscscan.com/tx/{transaction['hash']}"
            dogOut[hashLink] = txDate

        if transaction['methodId'] == dogBusdCreditingMethodId and transaction['isError'] == '0':
            txDate = datetime.utcfromtimestamp(int(transaction['timeStamp'])).strftime('%Y-%m-%d %H:%M:%S')
            hashLink = f"Tx Link - https://bscscan.com/tx/{transaction['hash']}"
            dogBusdOut[hashLink] = txDate

        if transaction['methodId'] == dogWbnbCreditingMethodId and transaction['isError'] == '0':
            txDate = datetime.utcfromtimestamp(int(transaction['timeStamp'])).strftime('%Y-%m-%d %H:%M:%S')
            hashLink = f"Tx Link - https://bscscan.com/tx/{transaction['hash']}"
            dogWbnbOut[hashLink] = txDate

        if transaction['methodId'] == afpClaimMethodId and transaction['isError'] == '0':
            txDate = datetime.utcfromtimestamp(int(transaction['timeStamp'])).strftime('%Y-%m-%d %H:%M:%S')
            hashLink = f"Tx Link - https://bscscan.com/tx/{transaction['hash']}"
            afpIn[hashLink] = txDate

        if transaction['functionName'] == afdClaimFunctionName and transaction['isError'] == '0':
            txDate = datetime.utcfromtimestamp(int(transaction['timeStamp'])).strftime('%Y-%m-%d %H:%M:%S')
            hashLink = f"Tx Link - https://bscscan.com/tx/{transaction['hash']}"
            afdIn[hashLink] = txDate

        if transaction['methodId'] == afdLpClaimMethodId and transaction['isError'] == '0':
            txDate = datetime.utcfromtimestamp(int(transaction['timeStamp'])).strftime('%Y-%m-%d %H:%M:%S')
            hashLink = f"Tx Link - https://bscscan.com/tx/{transaction['hash']}"
            afdLpIn[hashLink] = txDate

    return {'pigOut': pigOut, 'pigLpOut': pigLpOut, 'dogOut': dogOut, 'dogBusdOut': dogBusdOut, 'dogWbnbOut': dogWbnbOut,
            'afpIn': afpIn, 'afdIn': afdIn, 'afdLpIn': afdLpIn,}
