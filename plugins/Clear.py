from cybot import client, utils


@utils.register_command(name='clear')
@utils.admin
async def clear_messages(message, args):
    """
    <number>: clears given number of messages [Admins only]
    """
    try:
        await client.purge_from(message.channel, limit=min(100, int(' '.join(args))))
    except Exception as e:
        print(e)
        await client.send_message(message.channel, message.author.mention + " can't do that, sorry.")
