from uuid import uuid4

from calc_cmd import calc_cmd
from char_cmds import ord_cmd, chr_cmd
from ddg_cmd import query_ddg
from number_bases import hex_to_dec_cmd, dec_to_hex_cmd, num_converter_cmd
from rand_cmd import rand_cmd
from urban_cmd import query_urban_dictionary

doc_file = open('help_file.txt')
doc_str = doc_file.read()
doc_file.close()


def help_cmd(client, message, args):
    msg = "Available commands:\n[" + ", ".join(commands.keys()) + "]"
    return msg
	

def documentation_cmd(client, message, args):
	return doc_str


def test_command(client, message, args):
    return 'testing, args: ' + args


def bill_cmd(client, message, args):
    return 'http://belikebill.azurewebsites.net/billgen-API.php?default=1&name={}&sex=m' \
        .format(message.author.display_name)


def uuid_cmd(client, message, args):
    return str(uuid4())


commands = {
    # 'test': test_command,
    'help': help_cmd,
	'doc': documentation_cmd
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
}
