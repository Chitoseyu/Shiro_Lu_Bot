import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='[')

@bot.event
async def on_ready():
    print(" >> Bot is Online << ")

@bot.event
async def on_member_join(member):
   channel = bot.get_channel(604147926255665172)
   await channel.send(f'{member} Join!')

@bot.event
async def on_member_remove(member):
   channel = bot.get_channel(604149341145268234)
   await channel.send(f'{member} Leave!')

@bot.command()
async def ping(ctx):
    await ctx.send(f'{round(bot.latency*1000)} (ms)')

bot.run('NjAzOTQ2NzUxNzE1NzA0ODUy.XTpobg.4mxfhcKdSJCffYD3Qz7WhaA6DHM')    