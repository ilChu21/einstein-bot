import nextcord
from nextcord.ext import commands
from nextcord import Interaction


class Innovative(commands.Cog):

    def __init__(self, client):
        self.client = client



    @nextcord.slash_command(
        name='qr_invite',
        description='QR code invitation link to Innovative Innvestors Discord Server.'
    )

    async def qrInvite(self, interaction:Interaction):
        imageLink = "https://cdn.discordapp.com/attachments/1001892605551988886/1001892698845876274/DiscordQR.jpg"
        await interaction.response.send_message(imageLink)


def setup(client):
    client.add_cog(Innovative(client))