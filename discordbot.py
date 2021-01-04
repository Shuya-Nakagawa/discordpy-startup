from discord.ext import commands
import discord
import os
import traceback

token = os.environ['DISCORD_BOT_TOKEN']
bot = commands.Bot(command_prefix='/')
client = discord.Client();


@bot.command(name="こんにちは")
async def hello(ctx):
    await ctx.send(f"どうも、{ctx.message.author.name}さん！")


@bot.command(name="さようなら")
async def goodbye(ctx):
    await ctx.send(f"じゃあね、{ctx.message.author.name}さん！")


# 取得したトークンを「TOKEN_HERE」の部分に記入
bot.run('token')
