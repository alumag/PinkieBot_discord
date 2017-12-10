import os
import sys
import random
import string
import discord
import asyncio

from collections import namedtuple


DIR = os.path.dirname(__file__) + '/'
TOKEN_PATH = 'token.txt'
USER_KICK_TIMEOUT = 700
CMD_SIGN = '$'

if len(sys.argv) > 1:
    TOKEN_PATH = sys.argv[1]
TOKEN = open(TOKEN_PATH).read().strip('\n')

MemberOnServer = namedtuple('MemberOnServer', 'user server')

client = discord.Client()
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
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))


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


@client.event
async def on_message(message):
    member = MemberOnServer(user=message.author, server=message.server)
    if member in unverified.keys():
        if message.content == unverified[member]:
            await client.send_message(message.channel, member.user.mention + ' thanks!')
            unverified.pop(member)


client.run(TOKEN)
