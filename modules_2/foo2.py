import discord
from discord.ext import commands
class Example(commands.Cog):
    def __init__(self, client):
        self.client = client
    @commands.Cog.listener()
    async def on_message(self, message):
        username = str(message.author).split('#')[0]
        user_message = str(message.content)
        channel = str(message.channel)
        print(f'{username}: {user_message} ({channel})')
        if message.author == self.client.user:
            return
    @commands.command() # Actually introducing a command.
    async def hello(self, ctx:commands.Context):
        await ctx.send(f'Hello {ctx.author}')
def setup(client):
    client.add_cog(Example(client))
