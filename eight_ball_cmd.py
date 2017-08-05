import random


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
        return random.choice(ANSWERS)
    return 'Please ask a question'
