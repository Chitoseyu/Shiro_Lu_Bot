import discord
import json,asyncio,datetime
from discord.ext import commands
from core.classes import Cog_Extension

class Task(Cog_Extension):
   def __init__(self,*args,**kwargs):
       super().__init__(*args,**kwargs)

def setup(bot):
    bot.add_cog(Task(bot))



