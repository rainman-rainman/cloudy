import discord,yt_dlp,pafy,os,asyncio
from dotenv import load_dotenv,find_dotenv
from discord.ext import commands
client=commands.Bot(command_prefix='/',intents=discord.Intents.all())
######################################[ UTIL ]#########################################
load_dotenv(find_dotenv())
def youTubeUrlToTitle(url):
    video_object=pafy.new(url)
    video_title=video_object.title
    return video_title
######################################[ DC COMMANDS ]#########################################
@client.command()
async def join(ctx):
    if ctx.author.voice is None:
        await ctx.send("Connect to a voice channel first")
    voice_channel=ctx.author.voice.channel
    if ctx.voice_client is None:
        await voice_channel.connect()
    else:
        await ctx.voice_client.move_to(voice_channel)
@client.command()
async def leave(ctx):
    await ctx.voice_client.disconnect()
@client.command()
async def info(ctx):
    await ctx.send("supported commands: /join, /play url, /pause, /resume.")
######################################[ AUTH ]#########################################
client.run(os.environ.get("TOKEN"))
######################################[ EOF ]#########################################f