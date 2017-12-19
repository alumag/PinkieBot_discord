from urllib.parse import quote_plus
from uuid import uuid4

from plugins.char_cmds import ord_cmd, chr_cmd
from plugins.clear_messages import clear_messages
from plugins.ddg_cmd import query_ddg
from plugins.define import define_cmd
from plugins.eight_ball_cmd import eight_ball_cmd
from plugins.emojiwrite import emojiwrite
from plugins.karma import add_karma_cmd, get_karma_cmd, set_karma_cmd, take_karma_cmd
from plugins.karma_store import buy_item
from plugins.number_bases import hex_to_dec_cmd, dec_to_hex_cmd, num_converter_cmd
from plugins.rand_cmd import rand_cmd
from plugins.urban_cmd import query_urban_dictionary

from cybot.settings import DOC_TXT
from cybot import client


def help_cmd(message, args):
    msg = "Available plugins:\n[" + ", ".join(commands.keys()) + "]"
    return msg


def documentation_cmd(message, args):
    return "```\n{}\n```".format(DOC_TXT)


def test_command(message, args):
    return 'testing, args: ' + args


def bill_cmd(message, args):
    return 'http://belikebill.azurewebsites.net/billgen-API.php?default=1&name={}&sex=m' \
        .format(quote_plus(message.author.display_name))


def uuid_cmd(message, args):
    return str(uuid4())


commands = {
    # 'test': test_command,
    'help': help_cmd,
    'doc': documentation_cmd,
    # 'calc': calc_cmd,
    'rand': rand_cmd,
    'ddg': query_ddg,
    'bill': bill_cmd,
    'urban': query_urban_dictionary,
    # 'uuid': uuid_cmd,
    'hex2dec': hex_to_dec_cmd,
    'dec2hex': dec_to_hex_cmd,
    'ord': ord_cmd,
    'chr': chr_cmd,
    'convert': num_converter_cmd,
    'def': define_cmd,
    '8ball': eight_ball_cmd,
    'give': add_karma_cmd,
    'take': take_karma_cmd,
    'setkarma': set_karma_cmd,
    'karma': get_karma_cmd,
    'writmoji': emojiwrite,
}

karma_store_cmds = {
    'buy': buy_item,
}

async_commands = {
    'clear': clear_messages
}