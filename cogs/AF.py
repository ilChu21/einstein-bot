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
                    description=f"Pigs Balance - {pigsBalance(wallet)}\nPigs/BUSD Balance - {pigsBusdBalance(wallet)}\nAFP Balance - {afpBalance(wallet)}\nAFP/BUSD Balance - {afpBusdBalance(wallet)}\nDogs Balance - {dogsBalance(wallet)}\nDogs/BUSD Balance - {dogsBusdBalance(wallet)}\nDogs/WBNB Balance - {dogsWbnbBalance(wallet)}\nAFD Balance - {afdBalance(wallet)}",
                    color=nextcord.Color.gold()
                )

                embed.set_author(
                    name=f"{interaction.user.name} - {wallet[:6]}...{wallet[-4:]}",
                    icon_url=interaction.user.avatar.url
                )

                userDetails = afCheck(wallet)


                embed.add_field(
                    name="Pigs (V1) Sent",
                    value=userDetails['pigOut']
                )

                embed.add_field(
                    name="Pigs LP (V1) Sent",
                    value=userDetails['pigLpOut']
                )

                embed.add_field(
                    name="AFP (V2) Recieved",
                    value=userDetails['afpIn']
                )

                embed.add_field(
                    name="Dogs (V1) Sent",
                    value=userDetails['dogOut']
                )

                embed.add_field(
                    name="Dogs/BUSD (V1) Sent",
                    value=userDetails['dogBusdOut']
                )

                embed.add_field(
                    name="Dogs/WBNB (V1) Sent",
                    value=userDetails['dogWbnbOut']
                )

                embed.add_field(
                    name="AFD (V2) Recieved",
                    value=userDetails['afdIn']
                )

                embed.add_field(
                    name="AFD LP (V2) Recieved",
                    value=userDetails['afdLpIn']
                )

                await interaction.followup.send(embed=embed, ephemeral=True)
        except:
            await interaction.followup.send("Not a valid BSC address! Please try again.", ephemeral=True)

def setup(client):
    client.add_cog(AF(client))
