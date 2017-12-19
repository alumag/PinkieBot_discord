import utils
from cybot import client


@utils.register_command(name='ping', channels=['bot'])
async def ping_cmd(message, args):
    """
    return a pong
    [END-D]
    """
    await client.send_message(message.channel, "Pong!")
