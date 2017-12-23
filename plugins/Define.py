import json
import string
import requests

from discord import Message

from cybot import client, utils

extra = '\'".,'
english = string.ascii_letters + string.whitespace + string.digits + extra
hebrew = 'אבגדהוזחטיכלמנסעפצקרשתךףםןץ' + string.whitespace + extra


@utils.register_command(name='def')
async def define_cmd(message: Message, args: [str]):
    """
    <query>: finds a definition for the query, supports English and Hebrew
    """
    if len(args) > 0:
        res = ''
        args = args[0]
        if all(c in english for c in args):
            # english
            url = 'http://api.wordnik.com:80/v4/word.json/%s/definitions?limit=200&includeRelated=true&' \
                  'sourceDictionaries=all&useCanonical=false&includeTags=false&' \
                  'api_key=a2a73e7b926c924fad7001ca3111acd55af2ffabf50eb4ae5' % args
            req = requests.get(url)
            req.encoding = 'utf-8'
            data = req.text
            try:
                decode = json.loads(data)
                res = decode[0]['text']
            except:
                res = "Not found"
            if len(res) > 200 or len(res) < 3:
                res = "Not found"

        elif all(c in hebrew for c in args):
            # hebrew
            url = 'https://milog.co.il/' + args
            req = requests.get(url)
            req.encoding = 'utf-8'
            data = req.text
            data = data.replace('"', "'")
            data = data.replace('''<div class='sr_e_index'>1.</div>''', '')
            res = data.split('''<div class='sr_e_para'><div class='sr_e_txt'>''')[1].split('</div>')[0]
            if 'sr_example' in res:
                res = res.split('<span')[0]
            bad_letters = '\\/;<>\n\r'
            if any(l in res for l in bad_letters):
                res = "Not found"
        if len(res) > 200 or len(res) < 3:
            res = "Not found"
        res = args + ': ' + res
    else:
        res = 'Illegal'
    await client.send_message(message.channel, res)
