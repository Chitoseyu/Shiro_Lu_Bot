import discord
import datetime
import pytz
from discord.ext import commands
from discord.ext.commands import MissingPermissions
from core.classes import Cog_Extension

intents = discord.Intents.all()
intents.members = True
bot = discord.Client(intents=intents)

class Main(Cog_Extension):

    @commands.command()
    async def ping(self,ctx):
        await ctx.send(f'{round(self.bot.latency*1000)} (ms)')
    
    @commands.command()
    async def hi(self,ctx):
        await ctx.send('What?')

    @commands.command()
    async def em(self,ctx):
        
        embed=discord.Embed(title="作者Web", url="https://chitoseyu.github.io/" , description="about the bot", color=0x1137ee,timestamp=datetime.datetime.now(pytz.timezone('Asia/Taipei')))
        embed.set_author(name="Chitoseyu", url="https://i.imgur.com/ygaCR2U.jpg", icon_url="https://i.imgur.com/iNtrx7P.png")
        embed.set_thumbnail(url="https://i.imgur.com/vXV374R.jpg")
        embed.add_field(name="Bot 功能", value="請使用 help 查看目前已開發功能")
        embed.set_footer(text="------------------END------------------")
        await ctx.send(embed=embed) 
   
    @commands.command()
    async def sayd(self,ctx,*,msg):
        await ctx.message.delete()
        await ctx.send(msg)

    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def clear(self,ctx,num:int):
        await ctx.channel.purge(limit=num+1)
    @clear.error
    async def clear_error(self, ctx, error):
      if isinstance(error, MissingPermissions):
        await ctx.send(f"你沒有權限進行這項操作哦⛔ ")

    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def DKF(self,ctx):
        await ctx.channel.purge(limit=21)
    @DKF.error
    async def DKF_error(self, ctx, error):
      if isinstance(error, MissingPermissions):
        await ctx.send(f"你沒有權限進行這項操作哦⛔ ")
      



async def setup(bot):
    await bot.add_cog(main(bot))