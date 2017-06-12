from random import randint


def rand_cmd(client, message, args):
    if len(args) < 2:
        return 'Illegal'
    num1 = args.split(' ')[0]
    num2 = args.split(' ')[1]
    if not (num1.isdigit() and num2.isdigit()):
        return 'Illegal'
    try:
        return 'Result: ' + str(randint(float(num1), float(num2)))
    except:
        return 'LOL?'
