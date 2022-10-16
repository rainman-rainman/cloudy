import discord,yt_dlp,pafy,os
from os.path import join, dirname
from dotenv import load_dotenv, find_dotenv
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
async def after(self, ctx):
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
    # embed.set_author(name="Rainman", url="", icon_url="")
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
    # Postponed TODO twitch integration
    # Postponed TODO build CI/CD pipeline and deploy to artefakt server (Docker or Kubernetes)
    ctx.voice_client.stop()
    currentURL=url
    if currentURL in playlist_urls: playlist_urls.remove(currentURL)
    FFMPEG_OPTIONS={
        'before_options':'-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5',
        'options':'-vn',
    }
    ydl_opts = {
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
    # await ctx.voice_client.play(discord.FFmpegOpusAudio(song_info["url"],**FFMPEG_OPTIONS))
    ctx.voice_client.play(
        discord.FFmpegOpusAudio(song_info["url"],**FFMPEG_OPTIONS),
        # after=lambda ex: asyncio.get_running_loop().create_task(after(ctx))
    )
    # ctx.voice_client.is_playing()
    # if(nextURL()):
    #     play(ctx,nextURL())
# songs = asyncio.Queue()
# play_next_song = asyncio.Event()
#
# @client.event
# async def on_ready():
#     print('client ready')
#
# async def audio_player_task():
#     while True:
#         play_next_song.clear()
#         current = await songs.get()
#         current.start()
#         await play_next_song.wait()
#
# def toggle_next():
#     client.loop.call_soon_threadsafe(play_next_song.set)
#
# @client.command(pass_context=True)
# async def play(ctx, url):
#     if not client.is_voice_connected(ctx.message.server):
#         voice = await client.join_voice_channel(ctx.message.author.voice_channel)
#     else:
#         voice = client.voice_client_in(ctx.message.server)
#
#     player = await voice.create_ytdl_player(url, after=toggle_next)
#     await songs.put(player)
#
# client.loop.create_task(audio_player_task())
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
@client.command()
async def embed(ctx):
    #TODO embedd wrapper
    embed=discord.Embed(
    title="Text Formatting",
        url="https://realdrewdata.medium.com/",
        description="Here are some ways to format text",
        color=discord.Color.blue())
    embed.set_author(name="RealDrewData", url="https://twitter.com/RealDrewData", icon_url="https://cdn-images-1.medium.com/fit/c/32/32/1*QVYjh50XJuOLQBeH_RZoGw.jpeg")
    embed.set_thumbnail(url="https://i.imgur.com/axLm3p6.jpeg")
    embed.add_field(name="*Italics*", value="Surround your text in asterisks (\*)", inline=False)
    embed.add_field(name="**Bold**", value="Surround your text in double asterisks (\*\*)", inline=False)
    embed.add_field(name="__Underline__", value="Surround your text in double underscores (\_\_)", inline=False)
    embed.add_field(name="~~Strikethrough~~", value="Surround your text in double tildes (\~\~)", inline=False)
    embed.add_field(name="`Code Chunks`", value="Surround your text in backticks (\`)", inline=False)
    embed.add_field(name="Blockquotes", value="> Start your text with a greater than symbol (\>)", inline=False)
    embed.add_field(name="Secrets", value="||Surround your text with double pipes (\|\|)||", inline=False)
    embed.set_footer(text="Learn more here: realdrewdata.medium.com")
    await ctx.send(embed=embed)
######################################[ AUTH ]#########################################
client.run(os.environ.get("TOKEN"))
######################################[  ]#########################################f