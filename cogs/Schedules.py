import datetime
from pytz import timezone
from nextcord.ext import commands, tasks
from dripFuncs import *
from br34pFuncs import *
from afFuncs import *
from apiPrices import *
from reservoirFuncs import *


class Schedules(commands.Cog):

    def __init__(self, client):
        self.client = client

    
    def getGuildChannels(self):
        guildChannels = []
        allGuildChannels = self.client.get_all_channels()
        for guildChannel in allGuildChannels:
            if str(guildChannel.guild.id).startswith("864") and str(guildChannel.guild.id).endswith("956"):
                guildChannels.append(guildChannel)
        return guildChannels


    @tasks.loop(minutes=5)
    async def schedule_5min_prices(self):
        channels = []
        channelStrings = []
        allChannels = self.getGuildChannels()

        for chan in allChannels:
            if "💲 | PRICES AS OF " in str(chan):
                priceCategory = chan
                priceStringCategory = str(chan)[0:17]
            if "BNB: $" in str(chan):
                channels.append(chan)
                channelStrings.append(str(chan)[0:6])
            if "Drip DEX: $" in str(chan):
                channels.append(chan)
                channelStrings.append(str(chan)[0:11])
            if "Drip PCS: $" in str(chan):
                channels.append(chan)
                channelStrings.append(str(chan)[0:11])
            if "AFP: $" in str(chan):
                channels.append(chan)
                channelStrings.append(str(chan)[0:6])
            if "Br34p: $"in str(chan):
                channels.append(chan)
                channelStrings.append(str(chan)[0:8])
            if "DROP: $"in str(chan):
                channels.append(chan)
                channelStrings.append(str(chan)[0:7])
            if "AFD: $"in str(chan):
                channels.append(chan)
                channelStrings.append(str(chan)[0:6])

        prices = [dripDEXPrice(), br34pPrice(), afpPCSPrice(), bnbPrice(), afdPCSPrice(), dropPrice(), dripPCSPrice()]

        for channel, priceFuncs, strings in zip(channels, prices, channelStrings):
            await channel.edit(name=f"{str(strings)}{priceFuncs}")

        tz = timezone('US/Eastern')
        now = datetime.datetime.now(tz)
        time = now.strftime("%I:%M %p")
        await priceCategory.edit(name=f"{priceStringCategory}{time} |")


    @commands.Cog.listener()
    async def on_ready(self):
        self.schedule_5min_prices.start()


def setup(client):
    client.add_cog(Schedules(client))