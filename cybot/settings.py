import sys

# find the token and parse it
TOKEN_PATH = 'token.txt'
with open(TOKEN_PATH) as TOKEN_SOUCRE:
    TOKEN = TOKEN_SOUCRE.read().strip('\n')

user_kick_timeout = 700
eng = "poiuytrewqlkjhgfdsamnbvcxz"
heb = "פםןוטארק'/ךלחיעכגדשצמנהבסז"

with open('help_file.txt') as help_file:
    DOC_TXT = help_file.read()
