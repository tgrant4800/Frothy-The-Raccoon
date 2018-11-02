import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import time

Client = discord.Client()
client = commands.Bot(command_prefix = "?")

chat_filter = ["TRASH"]
bypass_list = []

@client.event
async def on_ready():
    print("Bot is online and connected to Discord")

@client.event
async def on_message(message):
    contents = message.content.split(" ") #contents is a list type
    for word in contents:
        if word.upper() in chat_filter:
            if not message.author.id in bypass_list:
                try:
                    await client.send_message(message.channel, "Did somebody say TRASH??")
                except discord.errors.NotFound:
                    return
                   
                    
        

client.run("your-token")
