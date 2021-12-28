import discord
import json
import random
from discord.ext import commands
from core.classes import Cog_Extension


with open('setting.json','r',encoding='utf8') as jfile:
    jdata = json.load(jfile)


class React(Cog_Extension):
    @commands.Cog.listener()
    async def on_ready(self):
        channel = self.bot.get_channel(jdata['Normal_channel'])
        print('目前登入身份：',self.bot.user)
        await channel.send(f"我又回來啦(´∀`)")
    @commands.command()
    async def 隨便(self,ctx):
        random_pic = random.choice(jdata['pic'])
        await ctx.send(random_pic)
        # random_pic = random.choice(jdata['pic'])
        # pic = discord.File(random_pic)
        # await ctx.send(file=pic)
    @commands.command()
    async def 沒錢(self,ctx):
        random_pic = random.choice(jdata['Net_img'])
        await ctx.send(random_pic)

def setup(bot):
    bot.add_cog(React(bot))