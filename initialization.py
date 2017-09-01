import json
import asyncio
from pprint import pprint

import discord

FILE_NAME = "config.js"

try:
    open(FILE_NAME, 'x', encoding='UTF-8').close()
except FileExistsError:
    pass


def init_file(file_name):
    """
    write to the file blank config

    :param file_name: the name of the file
    :type file_name: str
    :return: None
    """

    role = discord.Role(name="Default-Role", server=discord.Server(id=0))
    channel = discord.Channel(name="Default-Channel", topic="Its the Default-Channel's topic, please change it", server=discord.Server(id=0), type=0)

    the_config = {'roles': [role], 'channels': [channel]}
    with open(file_name, 'w', encoding='UTF-8') as file:
        json.dump(the_config, file, default=to_json, indent=4, ensure_ascii=False)

    # for testing:
    """
    js = json.dumps(the_config, default=to_json, indent=2, ensure_ascii=False)
    new_obj = json.loads(js, object_hook=from_json)

    new_js = json.dumps(new_obj, default=to_json, indent=2, ensure_ascii=False)
    if js == new_js:
        print("all good!!")
    else:
        print("\n\njs:")
        print(js)
        print("\n\nnew_js:")
        print(new_js)
    """


async def load_config_to_server(client, file_name, server_id):
    """
    Loads the config from the file and implements the config to the server

    :param client: the discord's client object
    :type client: discord.Client
    :param file_name: the name of the file
    :type file_name: str
    :param server_id: the id of the server
    :type server_id: str
    :return: if success True else return False
    """

    with open(file_name, encoding='UTF-8') as file:
        obj = json.load(file, object_hook=from_json)  # type: dict

    roles, channels = obj.get('roles', []), obj.get('channels', [])

    for role in roles:  # type: discord.Role
        try:
            await client.create_role(client.get_server(server_id), **to_json(role)['__value__'])
            pprint(to_json(role)['__value__'])
            print("created role")
        except discord.Forbidden as e:
            # log it
            print("failed created role")
            return False


async def init_cmd(client, message, args):
    print("in cmd")
    print("bug on ubuntu...")
    # await load_config_to_server(client, FILE_NAME, message.server.id)


def to_json(obj):
    """
    Convert objects to json format

    :param obj: the object
    :return: json object as string
    """

    if isinstance(obj, discord.Role):
        [obj.__slots__.remove(to_remove)
         for to_remove in ['id', 'colour', 'managed', 'server', 'position']
         if to_remove in obj.__slots__]
        return \
            {
                '__class__': 'discord.Role',
                '__value__':
                    {
                        name: obj.__getattribute__(name)
                        for name in obj.__slots__
                    }
            }
    elif isinstance(obj, discord.Permissions):
        return \
            {
                '__class__': 'discord.Permissions',
                '__value__':
                    {
                        pram[0]: pram[1]
                        for pram in obj
                    }
            }
    elif isinstance(obj, discord.colour.Colour):
        return obj.value
    elif isinstance(obj, discord.Channel):
        [obj.__slots__.remove(to_remove)
         for to_remove in ['voice_members', 'id', 'server', 'position',
                           'is_private', 'bitrate', '_permission_overwrites']
         if to_remove in obj.__slots__]
        return \
            {
                '__class__': 'discord.Channel',
                '__value__':
                    {
                        name: obj.__getattribute__(name)
                        for name in obj.__slots__
                    }
            }
    elif isinstance(obj, discord.ChannelType):
        return str(obj)
    raise TypeError(repr(obj) + ' is not JSON serializable')


def from_json(obj):
    """
    Convert json format to objects

    :param obj: json object as string
    :return: the object
    """

    if '__class__' in obj:
        if obj['__class__'] == 'discord.Role':
            obj['__value__']['server'] = discord.Server(id=0)
            return discord.Role(**obj['__value__'])
        elif obj['__class__'] == 'discord.Permissions':
            return discord.Permissions(**obj['__value__']).value
        elif obj['__class__'] == 'discord.Channel':
            obj['__value__']['server'] = discord.Server(id=0)
            return discord.Channel(**obj['__value__'])
    return obj


if __name__ == "__main__":
    init_file(FILE_NAME)
