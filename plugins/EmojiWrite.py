import string
import inflect
from discord import Message

from cybot import utils, client


@utils.register_command(name='writmoji')
async def emojiwrite(message: Message, args: [str]):
    """
    <query>: 'Emojizes' the query
    """
    p = inflect.engine()
    args = ' '.join(args)
    msg = ""
    try:
        for char in args:
            if char in string.ascii_uppercase:
                msg += ':regional_indicator_{0}: '.format(char.lower())
            elif char in string.ascii_lowercase:
                msg += ':regional_indicator_{0}: '.format(char.lower())
            elif char in string.digits:
                msg += ':{0}: '.format(p.number_to_words(char))
            else:
                msg += char + " "
    except:
        pass
    await client.send_message(message.channel, msg)
