import discord
import json
from discord.ext import commands
from core.classes import Cog_Extension


intents = discord.Intents.all()
intents.members = True
bot = discord.Client(intents=intents)


with open('setting.json','r',encoding='utf8') as jfile:
    jdata = json.load(jfile)

class Event(Cog_Extension):
    @commands.Cog.listener()
    @bot.event
    async def on_member_join(self,member):
          channel = self.bot.get_channel(jdata['Welcome_channel'])   
          await channel.send(f"<@{member.id}> 你好呀⛩️ 記得把群名片改成遊戲內ID哦 (´ ▽ ` )ﾉ 歡迎你~" )
        

    @commands.Cog.listener()
    async def on_member_remove(self,member):
        channel = self.bot.get_channel(jdata['Left_channel'])
        await channel.send(f'{member} 離開了🚓 ...')

    @commands.Cog.listener()
    async def on_message(self,msg):
        if msg.content in (jdata['keyword']) and msg.author != self.bot.user:
            await msg.channel.send('你說什麼?！')


async def setup(bot):
   await bot.add_cog(event(bot))
