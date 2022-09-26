import nextcord
from nextcord.ext import commands
from nextcord import Interaction
from afFuncs import *
from afTransactions import *


class AF(commands.Cog):

    def __init__(self, client):
        self.client = client



    @nextcord.slash_command(
        name='af_crediting',
        description="Returns info about Animal Farm crediting."
    )

    async def afCreditingCommand(
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
            for wallet in addresses:
                embed = nextcord.Embed(
                    title=f"Animal Farm Crediting Summary",
                    description=f"Pigs Balance - {pigsBalance(wallet)}\n{dogsBalance(wallet)}\n{afpBalance(wallet)}\n{dogsBusdBalance(wallet)}\n{dogsWbnbBalance(wallet)}\n{pigsBusdBalance(wallet)}",
                    color=nextcord.Color.gold()
                )

                embed.set_author(
                    name=f"{interaction.user.name} - {wallet[:6]}...{wallet[-4:]}",
                    icon_url=interaction.user.avatar.url
                )

                userDetails = afCheck(wallet)

                embed.add_field(
                    name="Pigs (V1) Sent",
                    value=f"{userDetails['pigOut']})"
                )

                await interaction.followup.send(embed=embed, ephemeral=True)
        except:
            await interaction.followup.send("Not a valid BSC address! Please try again.", ephemeral=True)

def setup(client):
    client.add_cog(AF(client))
