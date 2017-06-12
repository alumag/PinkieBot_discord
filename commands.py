from calc_cmd import calc_cmd
from rand_cmd import rand_cmd


async def help_cmd(client, message, args):
    msg = "Available commands:\n[" + ", ".join(commands.keys()) + "]"
    await client.send_message(message.channel, msg)

async def test_command(client, message, args):
    await client.send_message(message.channel, 'testing, args: ' + args)

commands = {
    'test': test_command,
    'help': help_cmd,
    'calc': calc_cmd,
    'rand': rand_cmd,
}
