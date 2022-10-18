import discord,os
from dotenv import load_dotenv,find_dotenv
from discord.ext import commands
bot=commands.Bot(command_prefix='.',intents=discord.Intents.all())
load_dotenv(find_dotenv())
# for loop to find cogs folder
for filename in os.listdir('./modules'):
  if filename.endswith('.py'):
    bot.load_extension(f'modules.{filename[:-3]}')
bot.run(os.environ.get("TOKEN"))