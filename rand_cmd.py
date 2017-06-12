import string
from random import randint


async def rand_cmd(client, message, args):
    if len(args) < 2:
        await client.send_message(message.channel, 'Illegal')
        return
    num1 = args.split(' ')[0]
    num2 = args.split(' ')[1]
    if not (num1.isdigit() and num2.isdigit()):
        await client.send_message(message.channel, 'Illegal')
        return
    await client.send_message(message.channel, 'Result: ' + str(randint(float(num1), float(num2))))