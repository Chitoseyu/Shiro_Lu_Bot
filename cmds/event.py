import discord
import json
from discord.ext import commands
from core.classes import Cog_Extension



with open('setting.json','r',encoding='utf8') as jfile:
    jdata = json.load(jfile)

class Event(Cog_Extension):
    @commands.Cog.listener()
    async def on_member_join(self,member):
        channel = self.bot.get_channel(jdata['Welcome_channel'])
        await channel.send(f'{member} Join!')

    @commands.Cog.listener()
    async def on_member_remove(self,member):
        channel = self.bot.get_channel(jdata['Left_channel'])
        await channel.send(f'{member} Leave!')

    @commands.Cog.listener()
    async def on_message(self,msg):
        if msg.content in (jdata['keyword']) and msg.author != self.bot.user:
            await msg.channel.send('沒問題！')


def setup(bot):
    bot.add_cog(Event(bot))
