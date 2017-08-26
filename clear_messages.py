import discord
import utils


@utils.admin
async def clear_messages(client, message, args):
	try:
		await client.purge_from(message.channel, limit=min(100, int(args)))
	except Exception as e:
		print(e)
		await client.send_message(message.channel, message.author.mention + " can't do that, sorry.")
