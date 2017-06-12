import discord
import asyncio

import ddg_cmd

client = discord.Client()

token = open('token.txt').read().strip('\n')

async def test_command(client, message, args):
    await client.send_message(message.channel, 'testing, args: ' + args)

commands = {'test': test_command,
			'ddg': ddg_cmd.query_ddg}


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
        args = message.content.strip('$' + command + ' ')
        await commands[command](client, message, args)

        # if message.content.startswith('!test'):
        #     await client.send_message(message.channel, 'Here is you test message, @' + message.author.name)
        # elif message.content.startswith('!sleep'):
        #     await asyncio.sleep(5)
        #     await client.send_message(message.channel, 'Done sleeping')

client.run(token)
