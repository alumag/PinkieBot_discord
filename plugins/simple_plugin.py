import utils


@utils.register_command(name='ping', channels=['bot'])
async def ping_cmd(bot, message, args):
    """
    return a pong
    [END-D]
    """
    await bot.send_message(message.channel, "Pong!")