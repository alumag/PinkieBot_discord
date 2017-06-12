import string


async def calc_cmd(client, message, args):
    if len(args) < 2:
        return 'Example use:\n$calc 1 + 1'
    for c in args:
        if c not in string.digits and c not in ' /+-*()':
            return 'Hacking?'
    return str(eval(args))
