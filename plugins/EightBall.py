from functools import reduce

from discord import Message

from cybot import utils, client

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


@utils.register_command(name='8ball', channels=['bot'])
async def eight_ball_cmd(message: Message, args: [str]):
    """
    <question>: answers your question with pure magic!
    """
    args = ' '.join(args)
    if args.endswith('?'):
        index = (int(message.author.id) + reduce(lambda x, y: x + y, map(ord, args))) % len(ANSWERS)
        ans = ANSWERS[index]
    else:
        ans = 'Please ask a question'
    await client.send_message(message.channel, ans)
