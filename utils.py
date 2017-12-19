from functools import wraps


def admin(func):
    @wraps(func)
    def wrapped(message, args):
        if message.author.server.owner.top_role not in message.author.roles:
            return
        return func(message, args)
    return wrapped