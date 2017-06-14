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

        if command not in ['ddg', 'convert']:
            if message.channel.name != 'bot':
    	        return

        args = message.content.replace('$' + command + ' ', '', 1)
        if command in commands.keys():
            ret = commands[command](client, message, args)
            if type(ret) is str:
                await client.send_message(message.channel,
                                          message.author.mention + '\n' + commands[command](client, message, args))
            elif type(ret) is discord.Embed:
                await client.send_message(message.channel, message.author.mention, embed=ret)
        else:
            await client.send_message(message.channel,
                                      message.author.mention + '\n"${}" is not supported!'.format(command))


client.run(token)
