import nextcord
from nextcord.ext import commands
from nextcord import Interaction
from dripFuncs import *
from faucetFuncs import *
from bnbFuncs import *
from reservoirFuncs import *
from busdFuncs import *
from br34pFuncs import *
from apiPrices import *


class Drip(commands.Cog):

    def __init__(self, client):
        self.client = client



    @nextcord.slash_command(
        name='drip',
        description='Description of Drip.'
    )

    async def dripCommand(self, interaction:Interaction):
        await interaction.response.send_message("The DRIP Network is the first"+
    " deflationary daily ROI token that pays stakers and referrers from a tax "+
    "on transactions!\n\nMade up of 3 primary smart contracts:\n**Fountain** "+
    "- Native DEX where DRIP tokens can be bought or sold.\n\n**Faucet** "+
    r"- Staking contract that allows consistent 1% daily return of your DRIP "+
    r"(365% or 100k DRIP maximum payout) passively. Players can compound and "+
    "extend their earnings through deposits, hydrating (compounding) rewards "+
    "as well as through team based referrals.\n\n**Resevoir** - The DRIP "+
    "Network’s solution for players that want benefit from non inflationary "+
    "yield farming through adding liquidity to DRIP.\n\nThe DRIP token has a "+
    "10% tax on all transactions except for buys on the native DEX and a 5% "+
    "tax on hydrates. These taxes goes into the Tax Vault which is used to "+
    "pay the daily ROI and referral bonuses.\n\n**Whitepaper**:\n"+
    "https://drip.community/docs/DRIP_LIGHTPAPER_v0.8_Lit_Version.pdf")



    @nextcord.slash_command(
        name='drip_stats',
        description='Current stats for Drip.'
    )

    async def dripStatsCommand(self, interaction:Interaction):
        pcsAddress = '0xa0feB3c81A36E885B6608DF7f0ff69dB97491b58'

        if decimal.Decimal(dripDEXPrice()) > decimal.Decimal(dripPCSPrice()):
            dripDexPrice = f"{dripDEXPrice()} 👍"
            dripPcsPrice = f"{dripPCSPrice()} 👎"
        else:
            dripDexPrice = f"{dripDEXPrice()} 👎"
            dripPcsPrice = f"{dripPCSPrice()} 👍"

        embed = nextcord.Embed(
            title="Drip Network Stats",
            description=f"Total Drip Supply: {round(totalDripSupply(), 3)}\nTotal Drip Players: {totalDripPlayers()}",
            color=nextcord.Color.blue()
        )

        embed.add_field(
            name="PancakeSwap",
            value=f"PCS Price: ${dripPcsPrice}\nPCS Drip Supply: {round(currentPCSSupply(), 3)}\nPCS BUSD Supply: {round(busdBalance(pcsAddress), 3)}",
            inline=True
        )

        embed.add_field(
            name="Fountain",
            value=f"Fountain Price: ${dripDexPrice}\nFountain Drip Supply: {round(currentFountainSupply(), 3)}\nFountain BNB Supply: {round(fountainBnbBalance(), 3)}",
            inline=False
        )

        embed.add_field(
            name="Faucet",
            value=f"\nFaucet Players: {totalFaucetPlayers()}\nTax Vault Drip Supply: {round(taxPoolBalance(), 3)}",
            inline=False
        )

        embed.add_field(
            name="Reservoir",
            value=f"Reservoir Players: {reservoirUsers()}\nReservoir Drop Supply: {round(totalDrop(), 3)}\nLocked Drop: {round(lockedDrop(), 3)}",
            inline=False
        )
        
        await interaction.response.send_message(embed=embed)



    @nextcord.slash_command(
        name='drip_account_lookup',
        description="Privately view current Drip details for personal account(s)."
    )

    async def dripAccountLookupCommand(
        self,
        interaction:Interaction,
        arg:str = nextcord.SlashOption(
            name="addresses",
            description="Enter public address(es) separated by a comma (,).",
            required=True
        )
    ):
        await interaction.response.defer(ephemeral=True)
        try:
            addresses = arg.replace(" ", "").split(',')
            totalDeposits = 0
            totalAvailable = 0
            totalDripBalance = 0
            totalBnbBalance = 0
            totalBusdBalance = 0
            totalMaxPayout = 0
            totalPrincipal = 0
            totalClaimed = 0
            totalHydrates = 0
            totalNDV = 0
            totalRemMaxPayout = 0
            
            count = 1

            if decimal.Decimal(dripDEXPrice()) > decimal.Decimal(dripPCSPrice()):
                bestPrice = dripDEXPrice()
            else:
                bestPrice = dripPCSPrice()

            for wallet in addresses:
                br34p = br34pBalance(wallet)

                embed = nextcord.Embed(
                    title=f"Drip Account {count} Summary",
                    description=f"Drip Balance - {dripBalance(wallet):.3f} (${dripBalance(wallet) * decimal.Decimal(bestPrice):.2f})\nBR34P Balance - {br34pBalance(wallet):.3f} (${br34pBalance(wallet) * decimal.Decimal(br34pPrice()):.2f}) (/)\nDROP Balance - {dropBalance(wallet):.3f}\nBNB Balance - {bnbBalance(wallet):.3f} (${bnbBalance(wallet) * decimal.Decimal(bnbPrice()):.2f})\nBUSD Balance - {busdBalance(wallet):.3f} (${busdBalance(wallet) * decimal.Decimal(busdPrice()):.2f})",
                    color=nextcord.Color.blue()
                )

                embed.set_author(
                    name=f"{interaction.user.name} - {wallet[:6]}...{wallet[-4:]}",
                    icon_url=interaction.user.avatar.url
                )

                embed.set_footer(
                    text=f"Drip DEX: ${dripDEXPrice()}\nDrip PCS: ${dripPCSPrice()}\nBNB: ${bnbPrice()}"
                )

                userDetails = walletDetails(wallet)
                totalPrincipal = totalPrincipal + userDetails['personalPrincipal']
                totalDeposits = totalDeposits + userDetails['deposits']
                totalAvailable = totalAvailable + userDetails['available']
                totalDripBalance = totalDripBalance + dripBalance(wallet)
                totalBnbBalance = totalBnbBalance + bnbBalance(wallet)
                totalBusdBalance = totalBusdBalance + busdBalance(wallet)
                totalMaxPayout = totalMaxPayout + userDetails['maxPayout']
                totalClaimed = totalClaimed + userDetails['claimed']
                totalHydrates = totalHydrates + userDetails['hydrates']
                totalNDV = totalNDV + userDetails['ndv']
                totalRemMaxPayout = totalRemMaxPayout + userDetails['remMaxPayout']


                embed.add_field(
                    name="Available",
                    value=f"{userDetails['available']:.3f}\n(${userDetails['available'] * decimal.Decimal(bestPrice):.2f})"
                )

                embed.add_field(
                    name="Deposits",
                    value=f"{userDetails['deposits']:.3f}\n(${userDetails['deposits'] * decimal.Decimal(bestPrice):.2f})"
                )

                embed.add_field(
                    name="NDV",
                    value=f"{userDetails['ndv']:.3f}\n(${userDetails['ndv'] * decimal.Decimal(bestPrice):.2f})"
                )

                embed.add_field(
                    name="Hydrates",
                    value=f"{userDetails['hydrates']:.3f}\n(${userDetails['hydrates'] * decimal.Decimal(bestPrice):.2f})"
                )

                embed.add_field(
                    name="Claimed",
                    value=f"{userDetails['claimed']:.3f}\n(${userDetails['claimed'] * decimal.Decimal(bestPrice):.2f})"
                )

                embed.add_field(
                    name="Max Payout",
                    value=f"{userDetails['maxPayout']:.3f}\n(${userDetails['maxPayout'] * decimal.Decimal(bestPrice):.2f})"
                )

                embed.add_field(
                    name="Daily Earnings",
                    value=f"{userDetails['deposits']*decimal.Decimal(0.01):.3f}\n(${userDetails['maxPayout'] * decimal.Decimal(bestPrice)/365:.2f})"
                )

                embed.add_field(
                    name="Monthly Earnings",
                    value=f"{(userDetails['deposits']*decimal.Decimal(0.01) * 30):.3f}\n(${userDetails['maxPayout'] * decimal.Decimal(bestPrice)/12:.2f})"
                )

                embed.add_field(
                    name="Remaining Max Payout",
                    value=f"{userDetails['remMaxPayout']:.3f}\n(${(userDetails['remMaxPayout']) * decimal.Decimal(bestPrice):.2f})"
                )

                embed.add_field(
                    name="Team Rewards Received",
                    value=f"{userDetails['teamRewards']:.3f}\n(${userDetails['teamRewards'] * decimal.Decimal(bestPrice):.2f})"
                )

                embed.add_field(
                    name="Airdrops Received",
                    value=f"{userDetails['airdropsR']:.3f}\n(${userDetails['airdropsR'] * decimal.Decimal(bestPrice):.2f})"
                )

                embed.add_field(
                    name="Airdrops Sent",
                    value=f"{userDetails['airdropsS']:.3f}\n(${userDetails['airdropsS'] * decimal.Decimal(bestPrice):.2f})"
                )

                embed.add_field(
                    name="Personal Principal",
                    value=f"{userDetails['personalPrincipal']:.3f}"
                )

                embed.add_field(
                    name="Drip Earned",
                    value=f"{userDetails['dripEarned']:.3f}\n(${userDetails['dripEarned'] * decimal.Decimal(bestPrice):.2f})"
                )

                embed.add_field(
                    name="Team",
                    value=f"{userDetails['referrals']}/{userDetails['totalStructure']}"
                )

                await interaction.followup.send(embed=embed, ephemeral=True)
                count += 1

            if len(addresses) > 1:
                embed = nextcord.Embed(
                    title=f"Total Accounts Summary - {len(addresses)} Wallets",
                    description=f"Total Drip Balance - {totalDripBalance:.3f} (${totalDripBalance * decimal.Decimal(bestPrice):.2f})\nTotal BNB Balance - {totalBnbBalance:.3f} (${totalBnbBalance * decimal.Decimal(bnbPrice()):.2f})\nTotal BUSD Balance - {totalBusdBalance:.3f} (${totalBusdBalance:.2f})",
                    color=nextcord.Color.blue()
                )

                embed.set_author(
                    name=interaction.user.name,
                    icon_url=interaction.user.avatar.url
                )

                embed.set_footer(
                    text=f"Drip DEX: ${dripDEXPrice()}\nDrip PCS: ${dripPCSPrice()}\nBNB: ${bnbPrice()}"
                )

                embed.add_field(
                    name="Total Available",
                    value=f"{totalAvailable:.3f}\n(${totalAvailable * decimal.Decimal(bestPrice):.2f})"
                )

                embed.add_field(
                    name="Total Deposits",
                    value=f"{totalDeposits:.3f}\n(${totalDeposits * decimal.Decimal(bestPrice):.2f})"
                )

                embed.add_field(
                    name="Total NDV",
                    value=f"{totalNDV:.3f}\n(${totalNDV * decimal.Decimal(bestPrice):.2f})"
                )

                embed.add_field(
                    name="Total Hydrates",
                    value=f"{totalHydrates:.3f}\n(${totalHydrates * decimal.Decimal(bestPrice):.2f})"
                )

                embed.add_field(
                    name="Total Claimed",
                    value=f"{totalClaimed:.3f}\n(${totalClaimed * decimal.Decimal(bestPrice):.2f})"
                )

                embed.add_field(
                    name="Total Max Payout",
                    value=f"{totalMaxPayout:.3f}\n(${totalMaxPayout * decimal.Decimal(bestPrice):.2f})"
                )

                embed.add_field(
                    name="Total Daily Earnings",
                    value=f"{totalDeposits*decimal.Decimal(0.01):.3f}\n(${totalMaxPayout * decimal.Decimal(bestPrice)/365:.2f})"
                )

                embed.add_field(
                    name="Total Monthly Earnings",
                    value=f"{(totalDeposits*decimal.Decimal(0.01)) * 30:.3f}\n(${totalMaxPayout * decimal.Decimal(bestPrice)/12:.2f})"
                )

                embed.add_field(
                    name="Total Remaining Max Payout",
                    value=f"{totalRemMaxPayout:.3f}\n(${totalRemMaxPayout * decimal.Decimal(bestPrice):.2f})"
                )

                embed.add_field(
                    name="Total Personal Principal",
                    value=f"{totalPrincipal:.3f}"
                )

                embed.add_field(
                    name="Total Drip Earned",
                    value=f"{totalDeposits - totalPrincipal:.3f}\n(${(totalDeposits - totalPrincipal) * decimal.Decimal(bestPrice):.2f})"
                )

                await interaction.followup.send(embed=embed, ephemeral=True)
        except:
            await interaction.followup.send("Not a valid BSC address! Please try again.", ephemeral=True)



def setup(client):
    client.add_cog(Drip(client))