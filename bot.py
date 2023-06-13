import discord
from discord.ext import commands, tasks
from discord.ext.commands import CommandNotFound
import json
import os
import asyncio
import logging


#intent = discord.Intents.default()
intent = discord.Intents.all()
intent.members = True

with open('setting.json', 'r', encoding='utf8') as jfile:
    jdata = json.load(jfile)

bot = commands.Bot(command_prefix='_', intents=intent)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')

@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Game(name='ニルギリ'))
   
        
@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, CommandNotFound):
        await ctx.send(f"🤖 沒有這個指令哦 ")
   ## raise error 


@bot.event
async def in_command_error(ctx, error):
    if isinstance(error, CommandNotFound):
        await ctx.send(f"🤖 沒有這個指令哦 ")
   ## raise error


@bot.event
async def CheckAnyFailure(checks, errors):
    raise checks


# # 載入指令程式檔案
# @bot.command()
# async def load(ctx, extension):
#     await bot.load_extension(f"cmds.{extension}")
#     await ctx.send(f"Loaded {extension} done.")

# # 卸載指令檔案
# @bot.command()
# async def unload(ctx, extension):
#     await bot.unload_extension(f"cmds.{extension}")
#     await ctx.send(f"UnLoaded {extension} done.")

# # 重新載入程式檔案
# @bot.command()
# async def reload(ctx, extension):
#     await bot.reload_extension(f"cmds.{extension}")
#     await ctx.send(f"ReLoaded {extension} done.")
  


async def cog_load_extensions():
   for Filename in os.listdir('./cmds'):
      if Filename.endswith('.py'):
         extension = Filename[:-3]
         try:
            print(f"Loaded extension cmds.{extension}")
            await bot.load_extension(f"cmds.{extension}")
            #bot.logger.info(f"Loaded extension '{extension}'")
         except Exception as e:
            exception = f"{type(e).__name__}: {e}"
            print(f"Failed to Loaded extension '{extension}' '{exception}'")
        #bot.logger.error(f"Failed to load extension {extension}\n{exception}")
     
async def main():
  await cog_load_extensions()
  #await bot.start(jdata['Token'])
     

if __name__ == "__main__":
    asyncio.run(main())
    bot.run(jdata['Token'])
  
