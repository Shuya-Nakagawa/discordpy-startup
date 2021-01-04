from discord.ext import commands
import discord
import os
import traceback

token = os.environ['DISCORD_BOT_TOKEN']
client = discord.Client();

# 接続に必要なオブジェクトを生成
client = discord.Client();
# メッセージ受信時に動作する処理
@client.event
async def on_message(message):
    # メッセージ送信者がBotだった場合は無視する
    if message.author.bot:
        return
    # 「/neko」と発言したら「にゃーん」が返る処理
    if message.content == '/neko':
        await message.channel.send('にゃーん')

bot.run(token)
