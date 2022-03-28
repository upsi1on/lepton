try :
	import urllib.request
	import functions.basic

except Exception as e :
	exit(str(e)[17:-1] + ' module is needed\n')

def start(url) :
	try :
		request = urllib.request.Request(url)
		request.add_header('User-Agent', functions.basic.getua() )
		request.get_method = lambda: 'HEAD'
		urllib.request.urlopen(request, timeout = 5)

	except KeyboardInterrupt :
		exit(' ~ Goodbye ;)\n')

	except Exception :
		return False

	else :
		return True