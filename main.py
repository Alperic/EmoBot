import discord
import aiohttp

client = discord.Client()

@client.event
async def on_ready():
    print('{0.user} olarak giriş yapıldı'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$add'):
        userInput = message.content[5:]
        if message.attachments:
            imageurl = message.attachments[0].url
            async with aiohttp.ClientSession() as session:
                async with session.get(imageurl) as response:
                    img = await response.read()
                await message.guild.create_custom_emoji(name=userInput, image=img, roles=None, reason=None)
                

        else:
            await message.channel.send('resim nerde knk')
        

#@client.event
#async def on_message(message):
#    if message.attachments:
#        await message.channel.send(content=message.attachments[0].url)


client.run('token')
