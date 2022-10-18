import discord,os
from dotenv import load_dotenv,find_dotenv
from discord.ext import commands
bot=commands.Bot(command_prefix='.',intents=discord.Intents.all())
@bot.event
async def on_ready():
    print("[SETUP ⚙️ ]: bot is ready to rock & roll 🚀")
load_dotenv(find_dotenv())
modules_dir=os.environ.get("MODULES_FOLDER_NAME")
print(f'[SETUP ⚙️ ]: modules directory name is {modules_dir}')
async def load(extension):
    await bot.load_extension(extension)
for filename in os.listdir('./'+modules_dir):
    if filename.endswith('.py'):
        load(modules_dir+'.'+filename[:-3])
        print(f'[SETUP ⚙️ ]: loaded module {filename[:-3]} from {modules_dir}/{filename} 🚀')
@bot.event
async def on_command_error(ctx, error):
   if isinstance(error, commands.CommandNotFound):
     await ctx.send('[ERROR ⚠️ ]: This command does not exist! .-.'+f"\n```{error}```")
bot.run(os.environ.get("TOKEN"))
