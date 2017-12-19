from random import randint
from discord import Message
from cybot import utils, client


@utils.register_command(name='rand', channels=['bot'])
async def rand_cmd(message: Message, args: [str]):
    """
    rand START END: generate a random number between START & END
    """
    if len(args) != 2:
        ans = 'Illegal'
    else:
        num1, num2 = args
        if num1.isdigit() and num2.isdigit():
            try:
                ans = 'Result: ' + str(randint(float(num1), float(num2)))
            except ValueError:
                ans = 'Illegal'
        else:
            ans = 'Illegal'
    await client.send_message(message.channel, ans)
