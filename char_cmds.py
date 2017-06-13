def ord_cmd(client, message, args):
    if len(args) != 1:
        return 'Illegal'
    try:
        dec = ord(args)
        hexa = hex(dec)
        return "'" + args + "' = " + str(dec) + " dec / " + hexa + " hex"
    except:
        return 'Illegal'


def chr_cmd(client, message, args):
    if 'x' in args:
        try:
            args = str(int(args, 16))
        except:
            return 'Illegal'
    if len(args) < 2 or not args.isdigit():
        return 'Illegal'

    try:
        return 'chr({}) = {}'.format(args, chr(int(args)))
    except:
        return '123'
