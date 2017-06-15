import discord
import asyncio

import urllib.request
import json

def query_ddg(client, message, args):

	try:
		query_data = urllib.request.urlopen(f'http://api.duckduckgo.com/?q={args}&format=json&pretty=1&skip_disambig=1').read()
		decoded_data = json.loads(query_data)

		results = decoded_data['Results']
		abstract = decoded_data['Abstract']

		print(not results)
		print(not abstract)

		if not abstract and results:
			embed = discord.Embed(title=args, description=f'{results[0]["FirstURL"]}', color=3447003)
		elif abstract and not results:
			embed = discord.Embed(title=args, description=f'{abstract}', color=3447003)
		else:
			query_data = urllib.request.urlopen(f'http://api.duckduckgo.com/?q=\{args}&format=json&pretty=1&skip_disambig=1&no_redirect=1').read()
			decoded_data = json.loads(query_data)
			embed = discord.Embed(title=f'{decoded_data["Redirect"]}', color=3447003)

		return embed
	except:
		return discord.Embed(title='Sorry', description='Could not find matching query', color=0xff5b4c)