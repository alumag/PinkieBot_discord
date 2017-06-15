import discord
import asyncio

import urllib.request
import json

def is_ascii(s):
    return all(ord(c) < 128 for c in s)

def query_ddg(client, message, args):

	try:
		if not is_ascii(args):
			args = urllib.request.quote(args)
		query_data = urllib.request.urlopen(f'http://api.duckduckgo.com/?q={args}&format=json&pretty=1&skip_disambig=1').read()
		decoded_data = json.loads(query_data)

		results = decoded_data['Results']
		abstract = decoded_data['Abstract']

		if not abstract and results:
			embed = discord.Embed(title=urllib.request.unquote(args), description=f'{results[0]["FirstURL"]}', color=3447003)
		elif abstract and not results:
			embed = discord.Embed(title=urllib.request.unquote(args), description=f'{abstract}', color=3447003)
		elif abstract and results:
			embed = discord.Embed(title=f"{urllib.request.unquote(results[0]['FirstURL'])}", description=f'{abstract}', color=3447003)
		else:
			query_data = urllib.request.urlopen(f'http://api.duckduckgo.com/?q=\{args}&format=json&pretty=1&skip_disambig=1&no_redirect=1').read()
			decoded_data = json.loads(query_data)

			if decoded_data['Redirect'].startswith('https://api.duckduckgo.com'):
				return discord.Embed(title='Sorry', description='Could not find matching query', color=0xff5b4c)

			embed = discord.Embed(title=f'{urllib.request.unquote(decoded_data["Redirect"])}', color=3447003)

		return embed
	except:
		return discord.Embed(title='Sorry', description='Could not find matching query', color=0xff5b4c)