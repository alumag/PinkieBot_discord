import discord
import asyncio
import re
import sys
from commands import commands, async_commands, karma_store_cmds
from karma import _take_karma
import random
import string

token_path = 'token.txt'
if len(sys.argv) > 1:
    token_path = sys.argv[1]

client = discord.Client()
token = open(token_path).read().strip('\n')

unverified = {}

user_kick_timeout = 700
eng = "poiuytrewqlkjhgfdsamnbvcxz"
heb = "פםןוטארק'/ךלחיעכגדשצמנהבסז"


async def destroy(member):
    await asyncio.sleep(user_kick_timeout)
    try:
        if member in unverified.keys():
            await client.send_message(member.server, "{0.mention} IT'S HAMMER TIME".format(member))
            await client.kick(member)
    except discord.Forbidden:
        await client.send_message(member.server, 'Member is too stronk')
    finally:
        unverified.pop(member)


def generate_captcha():
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))


@client.event
async def on_member_join(member):
    server = member.server
    fmt = "Welcome {0.mention}!\n Please type the following message in order to verify that you're a human: `{1}`"

    if member not in unverified.keys():
        captcha = generate_captcha()
        unverified[member] = captcha

        await client.send_message(server, server.owner.top_role.mention + '\n ' + fmt.format(member, captcha))
        await destroy(member)


@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')
    await client.change_presence(game=discord.Game(name="Cyber"))


@client.event
async def on_message(message):
    if re.match("^ע[ד]+[ ]*מת[י]+$", message.content):
        await client.send_message(message.channel, message.author.mention + '\nשתוק יצעיר פעור ולח')
        _take_karma(message.author.id)
        return

    if message.content.startswith('$'):
        command = message.content.strip('$').split(' ')[0]
        if all([*map(lambda c: (c in heb), command)]):
            command = ''.join([*map(lambda x: (eng[heb.index(x)]), command)])

        if command not in ['ddg', 'convert', 'clear', 'buy']:
            if 'bot' not in message.channel.name:
                tmp = await client.send_message(message.channel,
                                                message.author.mention + '"${}" is supported only on bot-related '
                                                                         'channels'.format(command))
                await asyncio.sleep(3)
                await client.delete_messages([tmp, message])
                return

        args = message.content.replace('$' + command + ' ', '', 1)
        if command in commands.keys():
            ret = commands[command](client, message, args)
            if type(ret) is str:
                await client.send_message(message.channel, message.author.mention + '\n' + ret)

            elif type(ret) is discord.Embed:
                await client.send_message(message.channel, message.author.mention, embed=ret)

        elif command in async_commands:
            await async_commands[command](client, message, args)

        elif 'karma-store' == message.channel.name:
            if command in karma_store_cmds:
                await karma_store_cmds[command](client, message, args)
            else:
                await client.delete_message(message)

        else:
            await client.send_message(message.channel,
                                      message.author.mention + '\n"${}" is not supported!'.format(command))

    elif 'karma-store' == message.channel.name:
        await client.delete_message(message)
    if message.author in unverified.keys():
        if message.content == unverified[message.author]:
            await client.send_message(message.channel,
                                      message.author.mention + ' thanks!')
            unverified.pop(message.author)


client.run(token)
