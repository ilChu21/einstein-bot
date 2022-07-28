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
        categoryInt = int(os.environ["PRICES_CATEGORY"])
        bnbChannelInt = int(os.environ["BNB_PRICE_CHANNEL"])
        dripDexChannelInt = int(os.environ["DRIP_DEX_PRICE_CHANNEL"])
        sripPcsChannelInt = int(os.environ["DRIP_PCS_PRICE_CHANNEL"])
        oozeChannelInt = int(os.environ["OOZE_PRICE_CHANNEL"])

        pricesCategory = self.client.get_channel(categoryInt)

        channels = {
            "BNB Price: $":bnbChannelInt,
            "Drip DEX Price: $":dripDexChannelInt,
            "Drip PCS Price: $":sripPcsChannelInt,
            "Ooze Price: $":oozeChannelInt
            }

        prices = [bnbPrice(), dripDEXPrice(), dripPCSPrice(), oozePrice()]

        for channel, priceFuncs in zip(channels, prices):

            channelID = self.client.get_channel(channels[channel])
            await channelID.edit(name=f"{channel}{priceFuncs}")

        now = datetime.datetime.now()
        time = now.strftime("%I:%M %p")
        await pricesCategory.edit(name=f"💲 | PRICES AS OF - {time} |")


    @commands.Cog.listener()
    async def on_ready(self):
        self.schedule_5min_prices.start()


def setup(client):
    client.add_cog(Schedules(client))