import discord
from discord.ext import commands

intents = discord.Intents.all()

bot = commands.Bot(command_prefix = "[" , intents = intents)

@bot.event
async def on_ready():
    print(">> Bot is online <<")

@bot.event
async def on_member_join(member):
    channel = bot.get_channel(1188057327690055680)
    await channel.send(f'{member} 重磅加入!')

@bot.event
async def on_member_remove(member):
    channel = bot.get_channel(1188057327690055680)
    await channel.send(f'{member} 悄悄的離開了!')

bot.run('MTE4Nzk2OTc5MjQ1MjMyOTYwMg.Guk89J.Ov5mhpNFOi7vE3qxXx7WgX3iEi0LkLCEo4J-tI')