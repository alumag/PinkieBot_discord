import os
import utils
import random
import string
import discord
import asyncio

from plugins import *
from cybot import client
from cybot.settings import (
    TOKEN,
    user_kick_timeout,
    eng, heb
)

from collections import namedtuple

DIR = os.path.dirname(__file__) + '/'
TOKEN_PATH = 'token.txt'
USER_KICK_TIMEOUT = 700
CMD_SIGN = '$'

MemberOnServer = namedtuple('MemberOnServer', 'user server')
Command = namedtuple('Command', 'function channels')

unverified = {}
commands = {}


async def destroy(member):
    await asyncio.sleep(USER_KICK_TIMEOUT)
    try:
        if member in unverified.keys():
            await client.send_message(member.server, "{0.mention} IT'S HAMMER TIME".format(member.user))
            await client.send_message(member.user, "You have been kicked from ***{}*** because you "
                                                   "didn't write the captcha".format(member.server))
            await client.kick(member.user)
            unverified.pop(member)
    except discord.Forbidden:
        await client.send_message(member.server, 'Member is too stronk')
        unverified.pop(member)


def generate_captcha():
    captcha = ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))

    if captcha.startswith(CMD_SIGN):
        return generate_captcha()
    else:
        return captcha


@client.event
async def on_member_join(user):
    if not user.bot:
        member = MemberOnServer(user=user, server=user.server)
        message = "Welcome {0.mention}!\n " \
                  "Please type the following message in order to verify that you're a human: `{1}`"

        if member not in unverified.keys():
            captcha = generate_captcha()
            unverified[member] = captcha

            await client.send_message(member.server,
                                      member.server.owner.top_role.mention + '\n ' +
                                      message.format(member.user, captcha))
            await destroy(member)


@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')
    await client.change_presence(game=discord.Game(name="Cyber"))


async def process_cmd(message):
    split = message.content[1:].split()
    cmd = split[0]
    args = split[1:]

    if all([*map(lambda c: (c in heb), cmd)]):
        cmd = ''.join([*map(lambda x: (eng[heb.index(x)]), cmd)])

    if cmd in commands.keys():
        if commands[cmd].channels is None or \
                any([utils.is_right_channel(message.channel.name, channel) for channel in commands[cmd].channels]):
            await commands[cmd].function(message, args)
        else:
            await client.send_message(message.channel, '**Oops...**  you can\'t use that command in this channel!')
    else:
        await client.send_message(message.channel, '**Oops...**  unknown command *{1}{0}* \n'
                                                   '(use {1}help to see the list of commands)'.format(cmd, CMD_SIGN))


@utils.register_command(name='help')
async def get_help(message, args):
    """
    Sends a 'help' message
    [END-D]
    """
    help_msg = "**__Help:__**\n\n"

    for command_name, command_func, command_channels in utils.register_command.functions_list:
        if hasattr(command_func, '__doc__') and isinstance(command_func.__doc__, str):
            doc = command_func.__doc__.split("[END-D]")[0].lstrip().rstrip()
        else:
            doc = ""
        help_msg += "**%s%s** - *%s*\n" % (CMD_SIGN, command_name, doc)
    await client.send_message(message.channel, help_msg)


@client.event
async def on_message(message):
    if message.author == client.user:
        return
    elif message.content.startswith(CMD_SIGN):
        await process_cmd(message)
    else:
        member = MemberOnServer(user=message.author, server=message.server)
        if member in unverified.keys():
            if message.content == unverified[member]:
                await client.send_message(message.channel, member.user.mention + ' thanks!')
                unverified.pop(member)

for cmd_name, cmd_func, cmd_channels in utils.register_command.functions_list:
    commands[cmd_name] = Command(function=cmd_func, channels=cmd_channels)

client.run(TOKEN)
