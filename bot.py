from discord.ext import commands
 
 
client = commands.Bot(command_prefix='?', case_insensitive=True)
 
 
@client.event
async def on_ready():
    print('Bot is online and connected to Discord')
 
 
@client.event
async def on_message(message):
    if client.user.id != message.author.id:
        if 'trash' in message.content:
            await message.channel.send('Did somebody say TRASH??')
 
 
client.run('NTA2OTY0NzcyNzY0NTE2MzUy.DsJe3g.hGXE78_OcE-ZeNaCGG5SMO-gd70')
