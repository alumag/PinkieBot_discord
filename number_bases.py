import discord
import string

def hex_to_dec_cmd(client, message, args):
    if len(args) < 2:
        return 'Illegal'
    try:
        result = str(int(args, 16))
        if '0x' not in args.lower():
            args = '0x' + args
        return args + ' = ' + result
    except:
        return 'Illegal'


def dec_to_hex_cmd(client, message, args):
    if len(args) < 2:
        return 'Illegal'
    try:
        num = int(args)
        return hex(num)
    except:
        return 'Illegal'

def num_converter_cmd(client, message, args):
    try:
        num = args.split(' ')[0]

        if num.startswith('0x'):
            decimal = int(num, 16)
            char = chr(decimal)
            octal = oct(decimal)
            binary = bin(decimal)
            hexa = num
        else:
            decimal = int(num)
            char = chr(decimal)
            octal = oct(decimal)
            binary = bin(decimal)
            hexa = hex(decimal)

        return discord.Embed(title='Conversion', description=f'Decimal: {decimal}\nHexadecimal: {hexa}\nOctal: {octal}\nBinary: {binary}\nUnicode: {char}', color=3447003)
    except:
        return discord.Embed(title='Sorry', description='Could not parse your query', color=0xff5b4c)