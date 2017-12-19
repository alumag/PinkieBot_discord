from discord import Message

from cybot import utils, client


@utils.register_command(name='ord', channels=['bot'])
async def ord_cmd(message: Message, args: [str]):
    """
    ord CHAR: display the ascii value of a CHAR
    """
    if len(args) != 1:
        ans = 'Illegal'
    else:
        try:
            dec = ord(args[0])
            hexa = hex(dec)
            ans = "'" + args[0] + "' = " + str(dec) + " dec / " + hexa + " hex"
        except:
            ans = 'Illegal'
    await client.send_message(message.channel, ans)


@utils.register_command(name='chr', channels=['bot'])
async def chr_cmd(message, args):
    """
    chr NUM: convert NUM to a char
    """
    if len(args) != 1:
        ans = 'Illegal'
    else:
        args = args[0]
        if 'x' in args:
            try:
                args = str(int(args, 16))
            except:
                ans = 'Illegal'
        if len(args) < 2 or not args.isdigit():
            ans = 'Illegal'

        try:
            ans = 'chr({}) = {}'.format(args, chr(int(args)))
        except:
            ans = '123'
    await client.send_message(message.channel, ans)

