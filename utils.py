from collections import namedtuple
from functools import wraps

Command = namedtuple('Command', 'name function channels')
ChannelName = namedtuple('ChannelName', 'string is_part')


def function_registerer():
    """
    create a list of functions from all the functions that @ that function
    name: str, the command that the function will assign to
    available_at=None: [str], list of channels that the command allowed in,
                  None = all, #text = exactly that name, text = text as part of the name
    """
    functions_list = []

    def registrar_warp(name, channels=None):
        if channels is None:
            the_channels = None
        else:
            the_channels = []
            for ch_name in channels:
                if ch_name.startswith('#'):
                    the_channels.append(ChannelName(string=ch_name[1:], is_part=False))
                else:
                    the_channels.append(ChannelName(string=ch_name, is_part=True))

        def registrar(func):
            functions_list.append(Command(name=name, function=func, channels=the_channels))
            return func

        return registrar

    registrar_warp.functions_list = functions_list
    return registrar_warp


def admin(func):
    @wraps(func)
    def wrapped(client, message, args):
        if message.author.server.owner.top_role not in message.author.roles:
            return
        return func(client, message, args)
    return wrapped


def is_right_channel(name_str, channel_name):
    if channel_name.is_part:
        return name_str in channel_name
    else:
        return name_str == channel_name.string


register_command = function_registerer()
