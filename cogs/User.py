import nextcord
from nextcord.ext import commands
from decouple import config




class User(commands.Cog):
    def __init__(self, client) -> None:
        self.client = client

    # for the message
    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author==self.client.user:
            return 
        await message.reply('Hello')

def setup(client):
    client.add_cog(User(client))