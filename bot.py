import discord,yt_dlp,pafy,os,asyncio
from dotenv import load_dotenv,find_dotenv
from discord.ext import commands
client=commands.Bot(command_prefix='/',intents=discord.Intents.all())
currentURL=""
playlist_urls=[]
######################################[ UTIL ]#########################################
load_dotenv(find_dotenv())
def youTubeUrlToTitle(url):
    video_object=pafy.new(url)
    video_title=video_object.title
    return video_title
def nextURL():
    return playlist_urls[0]
async def after(self,ctx):
    if not self.queue.empty() and not ctx.voice_client.is_playing():
        await pplay(ctx)
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
async def disconnect(ctx):
    await ctx.voice_client.disconnect()
@client.command()
async def list(ctx):
    msg=""
    if(currentURL and currentURL!=""):
        msg="**"+youTubeUrlToTitle(currentURL)+"**\n"
    for song_url in playlist_urls:
        msg=msg+youTubeUrlToTitle(song_url)+"\n"
    embed=discord.Embed(
    title="Playlist:",
        description="The songs that will be played next",
        color=discord.Color.blue())
    embed.add_field(name="titles:",value=msg,inline=False)
    await ctx.send(embed=embed)
@client.command()
async def nextup(ctx):
    await ctx.send(nextURL())
@client.command()
async def pplay(ctx):
    if(nextURL()):
        await play(ctx,nextURL())
@client.command()
async def play(ctx,url):
    ctx.voice_client.stop()
    currentURL=url
    if currentURL in playlist_urls: playlist_urls.remove(currentURL)
    FFMPEG_OPTIONS={
        'before_options':'-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5',
        'options':'-vn',
    }
    ydl_opts={
        'format':'bestaudio/best',
        'extractaudio':True,
        'audioformat':'mp3',
        'outtmpl':'%(extractor)s-%(id)s-%(title)s.%(ext)s',
        'restrictfilenames':True,
        'noplaylist':True,
        'nocheckcertificate':True,
        'ignoreerrors':False,
        'logtostderr':False,
        'quiet':True,
        'no_warnings':True,
        'default_search':'auto',
        'source_address':'0.0.0.0',
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        song_info=ydl.extract_info(currentURL,download=False)
    ctx.voice_client.play(
        discord.FFmpegOpusAudio(song_info["url"],**FFMPEG_OPTIONS),
    )
@client.command()
async def add(ctx,url):
    playlist_urls.append(url)
    await ctx.send("Added title: "+youTubeUrlToTitle(url))
@client.command()
async def pause(ctx):
    await ctx.voice_client.pause()
    await ctx.send("Paused.")
@client.command()
async def h(ctx):
    await ctx.send("supported commands: /join, /play url, /pause, /resume.")
@client.command()
async def resume(ctx):
    await ctx.voice_client.resume()
    await ctx.send("Resuming...")
######################################[ AUTH ]#########################################
client.run(os.environ.get("TOKEN"))
######################################[ EOF ]#########################################f