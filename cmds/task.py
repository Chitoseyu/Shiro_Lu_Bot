import discord
import re
import json, asyncio
from datetime import datetime
import pytz
from discord.ext import commands, tasks
from core.classes import Cog_Extension

time_zone = pytz.timezone('Asia/Taipei')

class Task(Cog_Extension):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)



    @commands.command()
    async def set_ch(self, ctx, ch: int):
        self.channel = self.bot.get_channel(ch)
        await ctx.send(f'設置成功(`･∀･)b～提醒頻道為：{self.channel.mention}')

    @commands.command()
    async def set_time(self, ctx, time):
        with open('setting.json', 'r', encoding='utf8') as jfile:
            jdata = json.load(jfile)
        if (re.search('^[0-9]{2}_[0-9]{2}_[0-9]{2}$', time)):
            jdata['time'] = time
            with open('setting.json', 'w', encoding='utf8') as jfile:
                json.dump(jdata, jfile, indent=6)
            await ctx.send(f'設置成功(`･∀･)b～提醒時間(時/分/秒)為：{time}')
        else:
            await ctx.send(f'設置失敗(；´Д`)！！提醒時間格式(時/分/秒)為 => HH_MM_SS')

    @commands.command()
    async def set_mes(self, ctx, mes):
        with open('setting.json', 'r', encoding='utf8') as jfile:
            jdata = json.load(jfile)
        jdata['message'] = mes
        with open('setting.json', 'w', encoding='utf8') as jfile:
            json.dump(jdata, jfile)
        await ctx.send(f'設置成功(`･∀･)b～提醒訊息為：{mes}')
    
    @commands.command()
    async def show_notes(self, ctx):
        with open('setting.json', 'r', encoding='utf8') as jfile:
            jdata = json.load(jfile)  
        
        notes_channel = jdata['Notion_channel']
        notes_time = jdata['time']
        notes_mes = jdata['message']

        fmt = '%Y-%m-%d'
        loc_dt = datetime.now(tz = time_zone)
        N_time = notes_time.replace('_',':')
        timeDay = loc_dt.strftime(fmt)
      
        self.channel = self.bot.get_channel(notes_channel)
        await ctx.send(f'嗨嗨(`･∀･)～目前的提醒訊息：')
        await ctx.send(f'提醒頻道：{self.channel.mention}')
        await ctx.send(f'提醒時間：{timeDay+ " " +N_time}')
        await ctx.send(f'提醒訊息：{notes_mes}')
        await ctx.send(f'若要更改設定記得透過指令哦(´∀`)~')
  

async def setup(bot):
   await bot.add_cog(Task(bot))
