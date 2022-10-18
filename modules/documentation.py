from discord.ext import commands
@commands.command()
async def info(ctx):
    await ctx.send("supported commands: /join, /play url, /pause, /resume.")
def setup(client):
    client.add_command(info)