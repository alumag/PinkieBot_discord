from urllib.parse import quote_plus
from discord import Message

from cybot import utils, client


@utils.register_command(name='bill', channels=['bot'])
async def bill_cmd(message: Message, args: [str]):
    """
    : Generates a bill meme with your name
    """
    await client.send_message(message.channel, 'http://belikebill.azurewebsites.net/billgen-API.php?default=1&name='
                                               '{}&sex=m'.format(quote_plus(message.author.display_name)))
