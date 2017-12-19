import string


def calc_cmd(message, args):
    if len(args) < 2:
        return 'Example use:\n$calc 1 + 1'
    for c in args:
        if c not in string.digits and c not in ' /+-*()j.':
            return 'Hacking?'
    try:
        return str(eval(args))
    except:
        return "Ayy something happened"
