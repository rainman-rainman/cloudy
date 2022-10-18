import discord,os
from dotenv import load_dotenv,find_dotenv
from discord.ext import commands
bot=commands.Bot(command_prefix='.',intents=discord.Intents.all())
load_dotenv(find_dotenv())
bot.load_extension("modules.music")
bot.load_extension("modules.documentation")
bot.load_extension("modules.moderation")
bot.run(os.environ.get("TOKEN"))