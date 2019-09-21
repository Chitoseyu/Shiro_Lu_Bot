import discord
import json,asyncio,datetime
from discord.ext import commands
from core.classes import Cog_Extension

class Task(Cog_Extension):
   def __init__(self,*args,**kwargs):
       super().__init__(*args,**kwargs)

def setup(bot):
    bot.add_cog(Task(bot))
'''       async def interval():
           await self.bot.wait_until_ready()
           self.channel = self.bot.get_channel()
           while not self.bot.is_closed():
                    await self
'''


