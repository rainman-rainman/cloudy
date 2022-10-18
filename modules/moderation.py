from discord.ext import commands
# --EVENTS--
class Events(commands.Cog):
  def __init__(self,bot):
    self.bot = bot
  # Bot online event
  @commands.Cog.listener()
  async def on_ready(self):
    print('GuhBot v3 is online and ready! C:')
  # Member joined Event
  @commands.Cog.listener()
  async def on_member_join(self,member):
    print(f'{member} joined the server. C:') 
  # Member left Event
  @commands.Cog.listener()
  async def on_member_remove(self,member):
    print(f'{member} left the server. :C')
# --MODERATION--
class Moderation(commands.Cog):
  def __init__(self,bot):
    self.bot=bot
  # clear command. default 5 messages,can be changed by user.
  @commands.command()
  async def clear(self,ctx,amount=5):
    await ctx.channel.purge(limit=amount+1)
# Cog Setup
def setup(bot):
  bot.add_cog(Events(bot))
  bot.add_cog(Moderation(bot))