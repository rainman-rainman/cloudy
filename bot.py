import discord,os
from dotenv import load_dotenv,find_dotenv
from discord.ext import commands
client=commands.Bot(command_prefix='.',intents=discord.Intents.all())
load_dotenv(find_dotenv())
client.load_extension("modules.music")
client.load_extension("modules.documentation")
client.run(os.environ.get("TOKEN"))