import discord,os
from dotenv import load_dotenv,find_dotenv
from discord.ext import commands
bot=commands.Bot(command_prefix='.',intents=discord.Intents.all())
load_dotenv(find_dotenv())
@bot.command()
async def load(ctx, extension):
  bot.load_extension(f'modules.{extension}')
  print(f'{extension} successfully loaded')
  ctx.send(f'{extension} successfully loaded')
# cog unloader command
@bot.command()
async def unload(ctx, extension):
  bot.unload_extension(f'modules.{extension}')
  print(f'{extension} successfully unloaded')
  ctx.send(f'{extension} successfully unloaded')
# cog reloader command, unload then load extenion
@bot.command()
async def reload(ctx, extension):
  bot.unload_extension(f'modules.{extension}')
  bot.load_extension(f'modules.{extension}')
  print(f'{extension} successfully re-loaded')
  ctx.send(f'{extension} successfully re-loaded')
# for loop to find cogs folder
for filename in os.listdir('./modules'):
  if filename.endswith('.py'):
    bot.load_extension(f'modules.{filename[:-3]}')
bot.run(os.environ.get("TOKEN"))