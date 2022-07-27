import nextcord
from nextcord.ext import commands
from nextcord import Interaction
from oozeFuncs import *


class Ooze(commands.Cog):

    def __init__(self, client):
        self.client = client



    @nextcord.slash_command(
        name='ooze_stats',
        description='Current Ooze Price'
    )


    async def oozePriceCommand(self, interaction:Interaction):
        await interaction.response.send_message(f"Ooze Price - ${oozePrice()}")


def setup(client):
    client.add_cog(Ooze(client))