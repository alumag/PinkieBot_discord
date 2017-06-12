import discord
import asyncio

import urllib.request
import json

async def query_ddg(client, message, args):
	query_data = urllib.request.urlopen(f'http://api.duckduckgo.com/?q={args}&format=json&pretty=1').read()

	decoded_data = json.loads(query_data)
	
	try:
		first_url = decoded_data['RelatedTopics'][0]

		txt = f'{first_url["FirstURL"]}\n {first_url["Text"]}'

		await client.send_message(message.channel, txt)
	except KeyError:
		pass