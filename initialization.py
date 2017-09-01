import json
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

    role = discord.Role(server=discord.Server(id=0))
    channel = discord.Channel(server=discord.Server(id=0))

    the_config = {'roles': [role], 'channels': [channel]}
    with open(file_name, 'w', encoding='UTF-8') as file:
        json.dump(the_config, file, default=to_json, indent=4, ensure_ascii=False)

    js = json.dumps(the_config, default=to_json, indent=2, ensure_ascii=False)
    js_role = json.loads(js, object_hook=from_json)

    new_js = json.dumps(js_role, default=to_json, indent=2, ensure_ascii=False)
    print(js == new_js)


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
         for to_remove in ['voice_members', 'id', 'server', 'position', 'is_private', 'bitrate']
         if to_remove in obj.__slots__]
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
    return obj


if __name__ == "__main__":
    init_file(FILE_NAME)

