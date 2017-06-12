import string


async def calc_cmd(client, message, args):
    if len(args) < 2:
        await client.send_message(message.channel, 'Example use:\n$calc 1 + 1')
        return
    for c in args:
        if c not in string.digits and c not in ' /+-*()':
            await client.send_message(message.channel, 'Hacking?')
            return
    await client.send_message(message.channel, str(eval(args)))
