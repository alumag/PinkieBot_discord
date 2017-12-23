import os

# find the token and parse it
TOKEN_PATH = 'token.txt'
with open(TOKEN_PATH) as TOKEN_SOURCE:
    TOKEN = TOKEN_SOURCE.read().strip('\n')

DIR = os.path.dirname(__file__) + '/'
CMD_SIGN = '%'

user_kick_timeout = 700
eng = "poiuytrewqlkjhgfdsamnbvcxz"
heb = "פםןוטארק'/ךלחיעכגדשצמנהבסז"
