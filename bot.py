from discord.ext import commands
 
 
client = commands.Bot(command_prefix='?')
 
 
@client.event
async def on_ready():
    print('Bot is online and connected to Discord')
 
@client.event
async def on_message(message):
    if client.user.id != message.author.id:
        if 'trash' in message.content:
            await message.channel.send('Did somebody say TRASH??')
 
 @client.event
async def on_message(message):
    if client.user.id != message.author.id:
        if 'book' in message.content:
            await message.channel.send('jaZ$GMBFUvetbmSER(PG&%Y*T&*GFNYGP%*NBGSUVEnGUSBN(REYbyfinvdfvaWERBSGFHAsDFBGHyJ7TYbrEvcgbTRsEBRgC *Frothy Ran Away*')
 
client.run('TOKEN')
