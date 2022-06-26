try :
	import urllib.request
	import functions.basic

except Exception as e :
	exit(str(e)[17:-1] + ' module is needed\n')

def start(url) :
	try :
		req = urllib.request.Request(
			url,
			data = None,
			headers = {
				'User-Agent': functions.basic.getua() ,
				'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
				'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
				'Accept-Language': 'en-US,en;q=0.8',
				'Connection': 'keep-alive'
			}
		)
		res = urllib.request.urlopen(req, timeout = 8)
		try :
			scode = res.read().decode('utf-8')

		except Exception :
			scode = res.read().decode('0x89')

		headers = res.info()
		code = res.getcode()
		return [scode, headers, code]

	except KeyboardInterrupt :
		exit(' ~ Goodbye ;)\n')

	except Exception :
		return False