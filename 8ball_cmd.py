import random


ANSWERS = [
    "Definitely",
    "Yes",
    "Probably",
    "Mabye",
    "Probably Not",
    "No",
    "Definitely Not",
    "I don't know",
    "Ask Later",
    "I'm too tired",
]

def 8ball_cmd(client, message, args):
    if message.endswith('?'):
        return random.choice(ANSWERS)
    return 'Please ask a question'
