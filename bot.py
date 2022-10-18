import discord,os
from dotenv import load_dotenv,find_dotenv
from discord.ext import commands
bot=commands.Bot(command_prefix='.',intents=discord.Intents.all())
load_dotenv(find_dotenv())
modules_dir=os.environ.get("MODULES_FOLDER_NAME")
print(f'[SETUP ⚙️]: modules directory name is {modules_dir}.')
async def setup():
    for filename in os.listdir('./'+modules_dir):
        if filename.endswith('.py'):
            await bot.load_extension(f'{modules_dir}.{filename[:-3]}')
            print(f'[SETUP ⚙️]: loaded module {filename[:-3]} from {modules_dir} 🚀')
bot.run(os.environ.get("TOKEN"))