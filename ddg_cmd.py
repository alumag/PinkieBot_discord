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

		if not abstract and results:
			embed = discord.Embed(title=args, description=f'{results[0]["FirstURL"]}', color=3447003)
		elif abstract and not results:
			embed = discord.Embed(title=args, description=f'{abstract}', color=3447003)
		elif not abstract and not results:
			related = decoded_data['RelatedTopics'][0]
			embed = discord.Embed(title=f'{related["FirstURL"]}', description=f'{related["Text"]}', color=3447003)
		else:
			embed = discord.Embed(title=f'{results[0]["FirstURL"]}', description=f'{abstract}', color=3447003)

		return embed
	except:
		return discord.Embed(title='Sorry', description='Could not find matching query', color=0xff5b4c)