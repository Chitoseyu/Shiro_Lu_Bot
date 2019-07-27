import discord
from discord.ext import commands
import json
import random

with open('setting.json','r',encoding='utf8') as jfile:
    jdata = json.load(jfile)

bot = commands.Bot(command_prefix='')

@bot.event
async def on_ready():
    print(" >> Bot is Online << ")

@bot.event
async def on_member_join(member):
   channel = bot.get_channel(jdata['Welcome_channel'])
   await channel.send(f'{member} Join!')

@bot.event
async def on_member_remove(member):
   channel = bot.get_channel(jdata['Left_channel'])
   await channel.send(f'{member} Leave!')

@bot.command()
async def ping(ctx):
    await ctx.send(f'{round(bot.latency*1000)} (ms)')

@bot.command()
async def 隨便(ctx):
    random_pic = random.choice(jdata['pic'])
    pic = discord.File(random_pic)
    await ctx.send(file=pic)
@bot.command()
async def cool(ctx):
     random_pic = random.choice(jdata['Net_img'])
     await ctx.send(random_pic)

bot.run(jdata['Token'])    