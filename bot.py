from discord.ext import commands
 
 
client = commands.Bot(command_prefix='?')
 
 
@client.event
async def on_ready():
    print('Bot is online and connected to Discord')
 
@client.event
async def on_message(message):
    if client.user.id != message.author.id:
        if 'trash' in message.content.lower():
            await message.channel.send('Did somebody say TRASH??')
    if client.user.id != message.author.id:
        if 'book' in message.content.lower():
            await message.channel.send('jaZ$GMBFUvetbmSER(PG&%Y*T&*GFNYGP%*NBGSUVEnGUSBN(REYbyfinvdfvaWERBSGFHAsDFBGHyJ7TYbrEvcgbTRsEBRgC *Frothy Ran Away*')
    if client.user.id != message.author.id:
        if 'garbage' in message.content.lower():
            await message.channel.send('{0.author.mention} is garbage.')
    if client.user.id != message.author.id:
        if 'communist' in message.content.lower():
            await message.channel.send('слава советской россии')
    if client.user.id != message.author.id:
        if 'communism' in message.content.lower():
            await message.channel.send('слава советской россии')
 
client.run('NTA2OTY0NzcyNzY0NTE2MzUy.DsJz_Q.Lf8kO_T_kehlMtBTaWgBayqwn4Y')
