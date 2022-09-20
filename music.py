from time import sleep
import discord
from discord import message
from discord.ext import commands
import youtube_dl
import random
import asyncio

from discord.ext.commands import bot


class music(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(help='connects bot to current voice channel (optional command)')
    async def join(self, ctx):
        if ctx.author.voice is None:
            await ctx.send(""" Not joining. You must be in VC before I come :smile: """)
        voice_channel = ctx.author.voice.channel
        if ctx.voice_client is None:
            await voice_channel.connect()
        else:
            await ctx.voice_client.move_to(voice_channel)

    @commands.command(help='disconnects bot from current voice channel')
    async def bye_bye(self, ctx):
        await ctx.send(""" (boombap successfully disconnected) """)
        await ctx.voice_client.disconnect()

    # alis for disconnect.
    @commands.command(help='disconnects bot from current voice channel')
    async def disconnect(self, ctx):
        await ctx.send(""" (boombap successfully disconnected) """)
        await ctx.voice_client.disconnect()

    # alis for disconnect.
    @commands.command(help='disconnects bot from current voice channel')
    async def d(self, ctx):
        await ctx.send(""" (boombap successfully disconnected) """)
        await ctx.voice_client.disconnect()


    @commands.command(help='!play (YT link), plays the youtube link (YT only)')
    async def play(self, ctx, url):

        if ctx.author.voice is None:
            await ctx.send(""" unsuccessful. (JOIN A VC FIRST!)""")
        voice_channel = ctx.author.voice.channel
        if ctx.voice_client is None:
            await voice_channel.connect()
        else:
            await ctx.voice_client.move_to(voice_channel)

        ctx.voice_client.stop()
        await ctx.send(f' Excellent Choice! now playing: {url}')
        FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5',
                          'options': '-vn'}
        YDL_OPTIONS = {'format': 'bestaudio'}
        vc = ctx.voice_client

        with youtube_dl.YoutubeDL(YDL_OPTIONS) as ydl:
            info = ydl.extract_info(url, download=False)
            url2 = info['formats'][0]['url']
            source = await discord.FFmpegOpusAudio.from_probe(url2, **FFMPEG_OPTIONS)
            vc.play(source)

    # alias for play
    @commands.command(help='!play (YT link), plays the youtube link (YT only)')
    async def p(self, ctx, url):

        if ctx.author.voice is None:
            await ctx.send(""" unsuccessful. (JOIN A VC FIRST!)""")
        voice_channel = ctx.author.voice.channel
        if ctx.voice_client is None:
            await voice_channel.connect()
        else:
            await ctx.voice_client.move_to(voice_channel)

        ctx.voice_client.stop()
        await ctx.send(f' Excellent Choice! now playing: {url}')
        FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5',
                          'options': '-vn'}
        YDL_OPTIONS = {'format': 'bestaudio'}
        vc = ctx.voice_client

        with youtube_dl.YoutubeDL(YDL_OPTIONS) as ydl:
            info = ydl.extract_info(url, download=False)
            url2 = info['formats'][0]['url']
            source = await discord.FFmpegOpusAudio.from_probe(url2, **FFMPEG_OPTIONS)
            vc.play(source)

    @commands.command(help='pauses song')
    async def pause(self, ctx):
        await ctx.send(""" (paused) """)
        await ctx.voice_client.pause()

    @commands.command(help='resumes song')
    async def resume(self, ctx):
        await ctx.send(""" (resumed) """)
        await ctx.voice_client.resume()


def setup(client):
    client.add_cog(music(bot))


