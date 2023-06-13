import discord
import time
from datetime import datetime
import pytz
from pytz import timezone 
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
        time_zone =  pytz.timezone('Asia/Taipei')
        fmt = '%Y-%m-%d %H:%M'
        loc_dt = datetime.now(tz = time_zone)
        timeS = loc_dt.strftime(fmt)
        print('現在系統時間：',timeS)
        await channel.send(f"現在時間：" + timeS + " , 我又回來啦(´∀`)")
        
    @commands.command()
    async def 隨便(self,ctx):
        random_pic = random.choice(jdata['pic'])
        await ctx.send(random_pic)

    @commands.command()
    async def 沒錢(self,ctx):
        random_pic = random.choice(jdata['Net_img'])
        await ctx.send(random_pic)

async def setup(bot):
   await bot.add_cog(React(bot))