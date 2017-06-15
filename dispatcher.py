import discord
import asyncio

from commands import commands

client = discord.Client()
token = open('token.txt').read().strip('\n')

main_server = 'SecHubIL'
main_channel = 'general'

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

    global main_server, main_channel

    for server in client.servers:
        if server.name == main_server:
            main_server = server
            break

    for channel in main_server.channels:
        if channel.name == main_channel:
            main_channel = channel
            break

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

@client.event
async def on_member_join(member):
    # print(dir(member))
    global main_server, main_channel

    await client.send_message(main_channel, f'Welcome ***{member.name}*** to SecHubIL!')

client.run(token)
