import string
from discord import Message

from cybot import utils, client

digits_to_words = {'0': 'zero', '1': 'one', '2':'two', '3':'three', '4':'four', '5':'five', '6':'six', '7':'seven','8':'eight',
                  '9': 'nine'}
@utils.register_command(name='writmoji')
async def emojiwrite(message: Message, args: [str]):
    """
    <query>: 'Emojizes' the query
    """
    args = ' '.join(args)
    msg = ""
    try:
        for char in args:
            if char in string.ascii_uppercase:
                msg += ':regional_indicator_{0}: '.format(char.lower())
            elif char in string.ascii_lowercase:
                msg += ':regional_indicator_{0}: '.format(char.lower())
            elif char in string.digits:
                msg += ':{0}: '.format(digits_to_words[char])
            else:
                msg += char + " "
    except:
        pass
    await client.send_message(message.channel, msg)
