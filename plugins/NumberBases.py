import discord
from discord import Message

from cybot import utils, client


@utils.register_command(name='hex2dec', channels=['bot'])
async def hex_to_dec_cmd(message: Message, args: [str]):
    """
    <value>: convert a hex value to decimal
    """
    if len(args) != 1:
        ans = 'Illegal'
    else:
        args = ' '.join(args)
        try:
            result = str(int(args, 16))
            if '0x' not in args.lower():
                args = '0x' + args
            ans = args + ' = ' + result
        except:
            ans = 'Illegal'
    await client.send_message(message.channel, ans)


@utils.register_command(name='dec2hex', channels=['bot'])
async def dec_to_hex_cmd(message: Message, args: [str]):
    """
    <number>: convert a decimal number to hexadecimal
    """
    if len(args) != 1:
        ans = 'Illegal'
    else:
        args = ' '.join(args)
        try:
            num = int(args)
            ans = args + ' = ' + hex(num)
        except:
            ans = 'Illegal'
    await client.send_message(message.channel, ans)


@utils.register_command(name='convert', channels=['bot'])
async def num_converter_cmd(message: Message, args: [str]):
    """
    <value>: display value in all representations
    """
    if len(args) == 1:
        try:
            num = args[0]

            if num.startswith('0x'):
                decimal = int(num, 16)
                char = chr(decimal)
                octal = oct(decimal)
                binary = bin(decimal)
                hexa = num
            elif num.isdigit():
                decimal = int(num)
                char = chr(decimal)
                octal = oct(decimal)
                binary = bin(decimal)
                hexa = hex(decimal)
            else:
                decimal = ord(num)
                char = num
                octal = oct(decimal)
                binary = bin(decimal)
                hexa = hex(decimal)

            embed = discord.Embed(title='Conversion',
                                  description=f'Decimal: {decimal}\nHexadecimal: {hexa}\nOctal: {octal}\nBinary: '
                                              f'{binary}\nUnicode: {char}',
                                  color=3447003)
        except:
            embed = discord.Embed(title='Sorry', description='Correct Usage: $convert <input>', color=0xff5b4c)
    else:
        embed = discord.Embed(title='Sorry', description='Correct Usage: $convert <input>', color=0xff5b4c)
    await client.send_message(message.channel, message.author.mention, embed=embed)
