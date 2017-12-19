import random
from functools import reduce

ANSWERS = [
    "Definitely",
    "Yes",
    "Probably",
    "Maybe",
    "Probably Not",
    "No",
    "Definitely Not",
    "I don't know",
    "Ask Later",
    "I'm too tired",
]

def eight_ball_cmd(client, message, args):
    if args.endswith('?'):
        index = (int(message.author.id) + reduce(lambda x,y: x + y, map(ord, args))) % len(ANSWERS)
        return ANSWERS[index]
    return 'Please ask a question'
