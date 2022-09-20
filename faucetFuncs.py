from unicodedata import decimal
from web3 import Web3
import json, decimal

bsc = "https://bsc-dataseed.binance.org/"
web3 = Web3(Web3.HTTPProvider(bsc))

faucetAddress = '0xFFE811714ab35360b67eE195acE7C10D93f89D8C'
faucetAbi = json.loads('[{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"_src","type":"address"},{"indexed":true,"internalType":"address","name":"_dest","type":"address"},{"indexed":false,"internalType":"uint256","name":"_deposits","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"_payouts","type":"uint256"}],"name":"BalanceTransfer","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"addr","type":"address"},{"indexed":true,"internalType":"address","name":"beneficiary","type":"address"}],"name":"BeneficiaryUpdate","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"addr","type":"address"},{"indexed":false,"internalType":"uint256","name":"timestamp","type":"uint256"}],"name":"Checkin","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"addr","type":"address"},{"indexed":true,"internalType":"address","name":"from","type":"address"},{"indexed":false,"internalType":"uint256","name":"amount","type":"uint256"}],"name":"DirectPayout","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"addr","type":"address"},{"indexed":false,"internalType":"uint256","name":"timestamp","type":"uint256"}],"name":"HeartBeat","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"addr","type":"address"},{"indexed":false,"internalType":"uint256","name":"interval","type":"uint256"}],"name":"HeartBeatIntervalUpdate","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"addr","type":"address"},{"indexed":false,"internalType":"uint256","name":"referrals","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"total_deposits","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"total_payouts","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"total_structure","type":"uint256"}],"name":"Leaderboard","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"addr","type":"address"},{"indexed":false,"internalType":"uint256","name":"amount","type":"uint256"}],"name":"LimitReached","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"addr","type":"address"},{"indexed":true,"internalType":"address","name":"manager","type":"address"},{"indexed":false,"internalType":"uint256","name":"timestamp","type":"uint256"}],"name":"ManagerUpdate","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"addr","type":"address"},{"indexed":true,"internalType":"address","name":"from","type":"address"},{"indexed":false,"internalType":"uint256","name":"amount","type":"uint256"}],"name":"MatchPayout","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"from","type":"address"},{"indexed":true,"internalType":"address","name":"to","type":"address"},{"indexed":false,"internalType":"uint256","name":"amount","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"timestamp","type":"uint256"}],"name":"NewAirdrop","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"addr","type":"address"},{"indexed":false,"internalType":"uint256","name":"amount","type":"uint256"}],"name":"NewDeposit","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"previousOwner","type":"address"},{"indexed":true,"internalType":"address","name":"newOwner","type":"address"}],"name":"OwnershipTransferred","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"addr","type":"address"},{"indexed":true,"internalType":"address","name":"upline","type":"address"}],"name":"Upline","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"addr","type":"address"},{"indexed":false,"internalType":"uint256","name":"amount","type":"uint256"}],"name":"Withdraw","type":"event"},{"stateMutability":"payable","type":"fallback"},{"inputs":[],"name":"CompoundTax","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"ExitTax","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"MAX_UINT","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"_to","type":"address"},{"internalType":"uint256","name":"_amount","type":"uint256"}],"name":"airdrop","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"","type":"address"}],"name":"airdrops","outputs":[{"internalType":"uint256","name":"airdrops","type":"uint256"},{"internalType":"uint256","name":"airdrops_received","type":"uint256"},{"internalType":"uint256","name":"last_airdrop","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"_addr","type":"address"}],"name":"balanceLevel","outputs":[{"internalType":"uint8","name":"","type":"uint8"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"checkin","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"claim","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"_addr","type":"address"}],"name":"claimsAvailable","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"contractInfo","outputs":[{"internalType":"uint256","name":"_total_users","type":"uint256"},{"internalType":"uint256","name":"_total_deposited","type":"uint256"},{"internalType":"uint256","name":"_total_withdraw","type":"uint256"},{"internalType":"uint256","name":"_total_bnb","type":"uint256"},{"internalType":"uint256","name":"_total_txs","type":"uint256"},{"internalType":"uint256","name":"_total_airdrops","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"_addr","type":"address"}],"name":"creditsAndDebits","outputs":[{"internalType":"uint256","name":"_credits","type":"uint256"},{"internalType":"uint256","name":"_debits","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"","type":"address"}],"name":"custody","outputs":[{"internalType":"address","name":"manager","type":"address"},{"internalType":"address","name":"beneficiary","type":"address"},{"internalType":"uint256","name":"last_heartbeat","type":"uint256"},{"internalType":"uint256","name":"last_checkin","type":"uint256"},{"internalType":"uint256","name":"heartbeat_interval","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"_upline","type":"address"},{"internalType":"uint256","name":"_amount","type":"uint256"}],"name":"deposit","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"deposit_bracket_size","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"dripVaultAddress","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"_addr","type":"address"}],"name":"getCustody","outputs":[{"internalType":"address","name":"_beneficiary","type":"address"},{"internalType":"uint256","name":"_heartbeat_interval","type":"uint256"},{"internalType":"address","name":"_manager","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"initialize","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"_addr","type":"address"},{"internalType":"uint8","name":"_level","type":"uint8"}],"name":"isBalanceCovered","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"_addr","type":"address"}],"name":"isNetPositive","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"_addr","type":"address"}],"name":"lastActivity","outputs":[{"internalType":"uint256","name":"_heartbeat","type":"uint256"},{"internalType":"uint256","name":"_lapsed_heartbeat","type":"uint256"},{"internalType":"uint256","name":"_checkin","type":"uint256"},{"internalType":"uint256","name":"_lapsed_checkin","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"_amount","type":"uint256"}],"name":"maxPayoutOf","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"pure","type":"function"},{"inputs":[],"name":"max_payout_cap","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"owner","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"_addr","type":"address"}],"name":"payoutOf","outputs":[{"internalType":"uint256","name":"payout","type":"uint256"},{"internalType":"uint256","name":"max_payout","type":"uint256"},{"internalType":"uint256","name":"net_payout","type":"uint256"},{"internalType":"uint256","name":"sustainability_fee","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"","type":"uint256"}],"name":"ref_balances","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"renounceOwnership","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"roll","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"_addr","type":"address"},{"internalType":"uint256","name":"_pendingDiv","type":"uint256"}],"name":"sustainabilityFeeV2","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"total_airdrops","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"total_bnb","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"total_deposited","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"total_txs","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"total_users","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"total_withdraw","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"newOwner","type":"address"}],"name":"transferOwnership","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"_newCompoundTax","type":"uint256"}],"name":"updateCompoundTax","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"_newBracketSize","type":"uint256"}],"name":"updateDepositBracketSize","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"_newExitTax","type":"uint256"}],"name":"updateExitTax","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256[]","name":"_newRefBalances","type":"uint256[]"}],"name":"updateHoldRequirements","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"_newInitialDeposit","type":"uint256"}],"name":"updateInitialDeposit","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"_newPayoutCap","type":"uint256"}],"name":"updateMaxPayoutCap","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"_newPayoutRate","type":"uint256"}],"name":"updatePayoutRate","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"_newRefBonus","type":"uint256"}],"name":"updateRefBonus","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"_newRefDepth","type":"uint256"}],"name":"updateRefDepth","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"_addr","type":"address"}],"name":"userInfo","outputs":[{"internalType":"address","name":"upline","type":"address"},{"internalType":"uint256","name":"deposit_time","type":"uint256"},{"internalType":"uint256","name":"deposits","type":"uint256"},{"internalType":"uint256","name":"payouts","type":"uint256"},{"internalType":"uint256","name":"direct_bonus","type":"uint256"},{"internalType":"uint256","name":"match_bonus","type":"uint256"},{"internalType":"uint256","name":"last_airdrop","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"_addr","type":"address"}],"name":"userInfoTotals","outputs":[{"internalType":"uint256","name":"referrals","type":"uint256"},{"internalType":"uint256","name":"total_deposits","type":"uint256"},{"internalType":"uint256","name":"total_payouts","type":"uint256"},{"internalType":"uint256","name":"total_structure","type":"uint256"},{"internalType":"uint256","name":"airdrops_total","type":"uint256"},{"internalType":"uint256","name":"airdrops_received","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"","type":"address"}],"name":"users","outputs":[{"internalType":"address","name":"upline","type":"address"},{"internalType":"uint256","name":"referrals","type":"uint256"},{"internalType":"uint256","name":"total_structure","type":"uint256"},{"internalType":"uint256","name":"direct_bonus","type":"uint256"},{"internalType":"uint256","name":"match_bonus","type":"uint256"},{"internalType":"uint256","name":"deposits","type":"uint256"},{"internalType":"uint256","name":"deposit_time","type":"uint256"},{"internalType":"uint256","name":"payouts","type":"uint256"},{"internalType":"uint256","name":"rolls","type":"uint256"},{"internalType":"uint256","name":"ref_claim_pos","type":"uint256"},{"internalType":"uint256","name":"accumulatedDiv","type":"uint256"}],"stateMutability":"view","type":"function"}]')

faucetContract = web3.eth.contract(address=faucetAddress, abi=faucetAbi)


def totalFaucetPlayers():
    return faucetContract.functions.total_users().call()

    
def walletDetails(address):
    address = web3.toChecksumAddress(address)
    users = faucetContract.functions.users(address).call()
    payouts = faucetContract.functions.payoutOf(address).call()
    airdrops = faucetContract.functions.airdrops(address).call()
    available = faucetContract.functions.claimsAvailable(address).call()
    available = web3.fromWei(available, 'ether')
    
    upline = users[0]
    referrals = users[1]
    totalStructure = users[2]
    teamRewards = web3.fromWei(users[3], 'ether') + web3.fromWei(users[4], 'ether')
    deposits = web3.fromWei(users[5], 'ether')
    depositTime = users[6]
    hydrates = web3.fromWei(users[8], 'ether')
    claimed = web3.fromWei(users[7], 'ether')
    
    maxPayout = web3.fromWei(payouts[1], 'ether')
    airdropsS = web3.fromWei(airdrops[0], 'ether')
    airdropsR = web3.fromWei(airdrops[1], 'ether')

    personalPrincipal = deposits - hydrates - teamRewards - airdropsR
    realClaims = claimed - (hydrates + (hydrates * decimal.Decimal(0.1))) - airdropsS
    ndv = (deposits + airdropsS + hydrates) - claimed
    remMaxPayout = maxPayout - claimed
    dripEarned = deposits - personalPrincipal
    
    return {'upline': upline, 'referrals': referrals, 'totalStructure': totalStructure, 'teamRewards': teamRewards, 
        'deposits': deposits, 'depositTime': depositTime, 'hydrates': hydrates, 'maxPayout': maxPayout, 
        'airdropsS': airdropsS, 'airdropsR': airdropsR, 'personalPrincipal': personalPrincipal, 'available': available, 'claimed': claimed, 'ndv': ndv, 'remMaxPayout': remMaxPayout, 'dripEarned': dripEarned, 'realClaims': realClaims}