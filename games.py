import sys
from time import sleep
import discord
from discord import message
from discord.ext import commands
import random
import asyncio

from discord.ext.commands import bot


### the following below the block is functions that are are misellaneous not related to music. ###

class games(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(help=""" States who the coolest member of the discord currently is.""")
    async def cool(self, ctx):
        users = ctx.guild.members
        user = str(random.choice(users)).split('#')[0]
        await ctx.send("currently... the coolest member on this server is: ")
        await ctx.send("3...")
        sleep(1)
        await ctx.send("2...")
        sleep(1)
        await ctx.send("1...")
        sleep(1)
        await ctx.send(f"`{user}`")
        await ctx.send(f"Wow, just hearing the name makes me shiver from their coolness! :cold_face:")

    @commands.command(help=""" RNG generator. """)
    async def random(self, ctx, args=None):
        
        await ctx.send("Welcome to The Pit! Calculating...")
        sleep(1.5)
        player1 = ctx.author.name
        
        await ctx.send("alright, let's do this...")
        sleep(2)
        p1_hand = str(random.randint(0, 20))
        await ctx.send(f"with RNG on their side, {player1} rolls a: `{p1_hand}`")
        


def setup(client):
    client.add_cog(games(bot))
