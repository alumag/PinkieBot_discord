import discord
import asyncio

import urllib.request
import json

async def query_ddg(client, message, args):

	try:
		query_data = urllib.request.urlopen(f'http://api.duckduckgo.com/?q={args}&format=json&pretty=1&skip_disambig=1').read()
		decoded_data = json.loads(query_data)

		results = decoded_data['Results']
		abstract = decoded_data['Abstract']

		if not abstract and results:
			txt = f'{results[0]["FirstURL"]}'
		elif abstract and not results:
			txt = f'{abstract}'
		elif not abstract and not results:
			related = decoded_data['RelatedTopics'][0]
			txt = f'{related["FirstURL"]}\n {related["Text"]}'
		else:
			txt = f'{results[0]["FirstURL"]}\n {abstract}'

		await client.send_message(message.channel, txt)
	except:
		await client.send_message(message.channel, "Sorry, I couldn't find anything on that")