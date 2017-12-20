import string

from discord import Message

from cybot import utils, client


@utils.register_command(name='writmoji')
async def emojiwrite(message: Message, args: [str]):
    """
    writmoji PHASE: write the phrase with emojies
    """
    args = ' '.join(args)
    msg = ""
    try:
        for char in args:
            if char in string.ascii_uppercase:
                msg += ':regional_indicator_{0}: '.format(char.lower())
            elif char in string.ascii_lowercase:
                msg += ':regional_indicator_{0}: '.format(char.lower())
            else:
                msg += char + " "
    except:
        pass
    await client.send_message(message.channel, msg)
