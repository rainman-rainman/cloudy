import discord,yt_dlp,pafy,os,asyncio
from discord.ext import commands
def youTubeUrlToTitle(url):
    video_object=pafy.new(url)
    video_title=video_object.title
    return video_title
@commands.command()
async def join(ctx):
    if ctx.author.voice is None:
        await ctx.send("Connect to a voice channel first")
    voice_channel=ctx.author.voice.channel
    if ctx.voice_client is None:
        await voice_channel.connect()
    else:
        await ctx.voice_client.move_to(voice_channel)
@commands.command()
async def leave(ctx):
    await ctx.voice_client.disconnect()
def setup(client):
    client.add_command(join)
    client.add_command(leave)