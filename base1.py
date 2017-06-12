token = 'MzIzODQxNzk3Nzk5NDExNzEz.DCBBOg.9k5s3K8JiWK6p5XDHvMSm_8Yulc'
import discord
import asyncio

client = discord.Client()

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

@client.event
async def on_message(message):
    if message.content.startswith('!test'):
        await client.send_message(message.channel, 'Here is you test message, @' + message.author.name)
    elif message.content.startswith('!sleep'):
        await asyncio.sleep(5)
        await client.send_message(message.channel, 'Done sleeping')

client.run(token)
