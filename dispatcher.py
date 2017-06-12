import discord
import asyncio
from commands import commands

client = discord.Client()
token = open('token.txt').read().strip('\n')


@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')


@client.event
async def on_message(message):
    if message.content.startswith('$'):
        command = message.content.strip('$').split(' ')[0]
        args = message.content.replace('$' + command + ' ', '', 1)
        if command in commands.keys():
            await commands[command](client, message, args)
            await client.send_message(message.channel, message.author.mention)
        else:
            await client.send_message(message.channel, message.author.mention + '\n"${}" is not supported!'.format(command))

client.run(token)
