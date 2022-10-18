from discord.ext import commands
@commands.command()
async def info(ctx):
    await ctx.send("supported commands: /join, /play url, /pause, /resume.")
def setup(bot):
    bot.add_command(info)