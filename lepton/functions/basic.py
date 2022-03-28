try :
	import random

except Exception as e :
	exit(str(e)[17:-1] + ' module is needed\n')

def httporhttps(url) :
	if url.startswith('http://') :
		return ['http', 4, url[7:]]
	if url.startswith('https://') :
		return ['https', 5, url[8:]]
	return False

def pwd() :
	pwd = __file__
	pwd = pwd.split('/')
	pwd.pop(len(pwd) - 1)
	return '/'.join(pwd)

def getua() :
	file = open(pwd() + '/../asset/ua')
	ua = file.read().split('\n')
	file.close()
	return random.choice(ua)