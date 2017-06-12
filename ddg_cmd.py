import discord
import asyncio

import urllib.request
import json

async def query_ddg(client, message, args):
	query_data = urllib.request.urlopen(f'http://api.duckduckgo.com/?q={args}&format=json&pretty=1').read()

	decoded_data = json.loads(query_data)
	
	try:
		first_url = decoded_data['RelatedTopics']
	except KeyError:
		pass