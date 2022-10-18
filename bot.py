import discord,os
from dotenv import load_dotenv,find_dotenv
from discord.ext import commands
bot=commands.Bot(command_prefix='.',intents=discord.Intents.all())
modules_dir={os.environ.get("MODULES_FOLDER_NAME")}
load_dotenv(find_dotenv())
for filename in os.listdir(f'./{modules_dir}'):
  if filename.endswith('.py'):
    bot.load_extension(f'{modules_dir}.{filename[:-3]}')
    print(f'[SETUP ⚙️]: loaded module {filename[:-3]} from {modules_dir} 🚀')
bot.run(os.environ.get("TOKEN"))
