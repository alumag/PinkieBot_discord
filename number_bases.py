def hex_to_dec_cmd(client, message, args):
    if len(args) < 2:
        return 'Illegal'
    try:
        result = str(int(args, 16))
        if '0x' not in args.lower():
            args = '0x' + args
        return args + '=' + result
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