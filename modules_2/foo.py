import discord
from discord.ext import commands
class MyCog(commands.Cog):
    def __init__(self,bot):
        self.bot=bot
    @commands.command()
    async def smt(self,ctx):
        await ctx.send("something")
def setup(bot):
    bot.add_cog(MyCog(bot))