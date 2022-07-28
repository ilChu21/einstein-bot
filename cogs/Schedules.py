import datetime, os
from nextcord.ext import commands, tasks
from faucetFuncs import *
from oozeFuncs import *
from bnbFuncs import *


class Schedules(commands.Cog):

    def __init__(self, client):
        self.client = client


    @tasks.loop(minutes=5)
    async def schedule_5min_prices(self):
        pricesCategory = self.client.get_channel(os.environ["PRICES_CATEGORY"])

        channels = {
            "BNB Price: $":os.environ["BNB_PRICE_CHANNEL"],
            "Drip DEX Price: $":os.environ["DRIP_DEX_PRICE_CHANNEL"],
            "Drip PCS Price: $":os.environ["DRIP_PCS_PRICE_CHANNEL"],
            "Ooze Price: $":os.environ["OOZE_PRICE_CHANNEL"]
            }

        prices = [bnbPrice(), dripDEXPrice(), dripPCSPrice(), oozePrice()]

        for channel, priceFuncs in zip(channels, prices):
            channelID = self.client.get_channel(channels[channel])
            await channelID.edit(name=f"{channel}{priceFuncs}")
            print(f"{channel}{priceFuncs}")

        now = datetime.datetime.now()
        time = now.strftime("%I:%M %p")
        await pricesCategory.edit(name=f"💲 | PRICES AS OF - {time} |")
        print(f"💲 | PRICES - {time} |\n")


    @commands.Cog.listener()
    async def on_ready(self):
        self.schedule_5min_prices.start()


def setup(client):
    client.add_cog(Schedules(client))