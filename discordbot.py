from discord.ext import commands
import discord
import os
import traceback

token = os.environ['DISCORD_BOT_TOKEN']
client = discord.Client()
bot = commands.Bot(command_prefix='＄')

@client.event()

async def on_message(message):

    if messeage.author.bot:
        return
    if messeage.content == '/ping':
        await message.channel.send('pong')
    if message.content == '/neko':
        await message.channel.send('にゃーん')

client.run('token')
