import string

def emojiwrite(client, message, args):
	msg = ""
	print("in")
	print(args)
	try:
		print(args)
		print(args[0])
		for char in args:
			print(char)
			print(msg)
			if char in string.ascii_uppercase:
				msg += ':regional_indicator_{0}: '.format(char.lower())
			elif char in string.ascii_lowercase:
				msg += ':regional_indicator_{0}: '.format(char.lower())
			else:
				msg += char + " "
	except:
		pass
	return msg

