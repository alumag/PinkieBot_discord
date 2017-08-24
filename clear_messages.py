import discord

async def clear_messages(client, message, args):
	if message.author.server.owner.top_role in message.author.roles:
		try:
			await client.purge_from(message.channel, limit=min(100, int(args)))
		except Exception as e:
			print(e)
			await client.send_message(message.channel, message.author.mention + " can't do that, sorry.")
