import discord
from discord.ext import commands
import music
import games

cogs = [music, games]

bot = commands.Bot(command_prefix='!', intents=discord.Intents.all())

for i in range(len(cogs)):
    cogs[i].setup(bot)

bot.run('Put your own bot key here!')
