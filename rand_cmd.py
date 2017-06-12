from random import randint


async def rand_cmd(client, message, args):
    if len(args) < 2:
        return 'Illegal'
    num1 = args.split(' ')[0]
    num2 = args.split(' ')[1]
    if not (num1.isdigit() and num2.isdigit()):
        return 'Illegal'
    return 'Result: ' + str(randint(float(num1), float(num2)))