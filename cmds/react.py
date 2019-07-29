import discord
import json
import random
from discord.ext import commands
from core.classes import Cog_Extension


with open('setting.json','r',encoding='utf8') as jfile:
    jdata = json.load(jfile)


class React(Cog_Extension):
    @commands.command()
    async def 隨便(self,ctx):
        random_pic = random.choice(jdata['pic'])
        pic = discord.File(random_pic)
        await ctx.send(file=pic)
    @commands.command()
    async def cool(self,ctx):
        random_pic = random.choice(jdata['Net_img'])
        await ctx.send(random_pic)

def setup(bot):
    bot.add_cog(React(bot))