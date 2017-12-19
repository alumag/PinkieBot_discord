from urllib.parse import quote_plus
import urllib.request
import json

from discord import Message
from cybot import utils, client


@utils.register_command(name='urban')
async def query_urban_dictionary(message: Message, args: [str]):
    """
    urban PHASE: search PHASE on urban (a dictionary)
    """
    ans = "Sorry, I couldn't find anything on that"
    if len(args) > 0:
        try:
            args = quote_plus(' '.join(args))
            query_data = urllib.request.urlopen(f'http://api.urbandictionary.com/v0/define?term={args}').read()
            decoded_data = json.loads(query_data)

            ans = f'**Word:** {decoded_data["list"][0]["word"]}\n{decoded_data["list"][0]["definition"]}'
        except:
            pass
    await client.send_message(message.channel, ans)
