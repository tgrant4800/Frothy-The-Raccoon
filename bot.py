import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import time

Client = discord.Client()
client = commands.Bot(command_prefix = "?")

@client.event
async def on_ready():
    print("Bot is online and connected to Discord")

@client.event
async def on_message(message):
    if client.user.id != message.author.id:
        if 'trash' in message.content:
            await client.send_message(message.channel, 'Did somebody say TRASH??')

    await client.process_commands(message)
    
client.run("")
