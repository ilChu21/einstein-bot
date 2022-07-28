import datetime
from nextcord.ext import commands, tasks
from faucetFuncs import *
from oozeFuncs import *
from bnbFuncs import *


class Schedules(commands.Cog):

    def __init__(self, client):
        self.client = client

    
    def guildChannels(self):
        for guild in self.client.guilds:
            if str(guild.id).startswith("864") and str(guild.id).endswith("956"):
                allGuildChannels = self.client.get_all_channels()
                return allGuildChannels


    @tasks.loop(minutes=5)
    async def schedule_5min_prices(self):
        channels = []
        channelStrings = []
        allChannels = self.guildChannels()

        for chan in allChannels:
            if "💲 | PRICES AS OF " in str(chan):
                priceCategory = chan
                priceStringCategory = str(chan)[0:17]
            if "BNB Price: $" in str(chan):
                channels.append(chan)
                channelStrings.append(str(chan)[0:12])
            if "Drip DEX Price: $" in str(chan):
                channels.append(chan)
                channelStrings.append(str(chan)[0:17])
            if "Drip PCS Price: $" in str(chan):
                channels.append(chan)
                channelStrings.append(str(chan)[0:17])
            if "Ooze Price: $" in str(chan):
                channels.append(chan)
                channelStrings.append(str(chan)[0:13])

        prices = [dripDEXPrice(), oozePrice(), bnbPrice(), dripPCSPrice()]

        for channel, priceFuncs, strings in zip(channels, prices, channelStrings):
            await channel.edit(name=f"{str(strings)}{priceFuncs}")

        now = datetime.datetime.now()
        time = now.strftime("%I:%M %p")
        await priceCategory.edit(name=f"{priceStringCategory}{time} |")


    @commands.Cog.listener()
    async def on_ready(self):
        self.schedule_5min_prices.start()


def setup(client):
    client.add_cog(Schedules(client))