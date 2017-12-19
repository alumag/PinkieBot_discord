import json
import string
import requests

extra = '\'".,'
english = string.ascii_letters + string.whitespace + string.digits + extra
hebrew = 'אבגדהוזחטיכלמנסעפצקרשתךףםןץ' + string.whitespace + extra


def define_cmd(client, message, args):
    if len(args) < 2:
        return 'Illegal'
    res = ''
    if all(c in english for c in args):
        # english
        url = 'http://api.wordnik.com:80/v4/word.json/%s/definitions?limit=200&includeRelated=true&sourceDictionaries=all&useCanonical=false&includeTags=false&api_key=a2a73e7b926c924fad7001ca3111acd55af2ffabf50eb4ae5' % args
        req = requests.get(url)
        req.encoding = 'utf-8'
        data = req.text
        decode = json.loads(data)
        try:
            res = decode[0]['text']
        except:
            return "Not found"
        if len(res) > 200 or len(res) < 3:
            return "Not found"

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
            return "Not found"
    if len(res) > 200 or len(res) < 3:
        return "Not found"
    res = args + ': ' + res
    return res
