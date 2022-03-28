try :
	import functions.urlcheck
	import functions.getcontent
	import functions.basic
	import sys
	import socket

except ModuleNotFoundError as e :
	exit(str(e)[17:-1] + ' module is needed\n')

except KeyboardInterrupt :
	exit(' ~ Goodbye ;)\n')

argv = sys.argv

try :

	def scan(url) :
		link = functions.basic.httporhttps(url)
		if link :
			link = link[0] + '://' + link[2].split('/')[0]
			if not functions.urlcheck.start(link) :
				exit('Unable connect to {}\n'.format(repr(functions.basic.httporhttps(link)[2])))

		else :
			link = url.split('/')[0]
			if functions.urlcheck.start('http://' + link) :
				link = 'http://' + link
			elif functions.urlcheck.start('https://' + link) :
				link = 'https://' + link

			else :
				exit('Unable connect to {}\n'.format(repr(argv[2].replace('https://', '').replace('http://', ''))))

		x = functions.getcontent.start(link)
		if x :
			link = link.replace('http://', '').replace('https://', '')
			ip = socket.gethostbyname(link)
			waf = ''
			if link != ip :
				print('Host : {} ({})\n'.format(link, ip))

			else :
				print('Host : {}\n'.format(link))

			if 'Via' in x[1].keys() or 'X-cache' in x[1].keys() and 'cloudfront' in str(x[1].lower()) :
				waf = 'CloudFront'

			elif 'cloudflare' in str(x[1]) :
				waf = 'CloudFlare'

			elif 'X-Iinfo' in x[1].keys() or x[1].get('X-CDN') == 'Incapsula' :
				waf = 'Incapsula'

			elif x[1].get('Server') == 'Sucuri/Cloudproxy' or 'X-Sucuri-ID' in x[1].keys() or 'X-Sucuri-Cache' in x[1].keys() or 'Access Denied - Sucuri Website Firewall' in x[0] :
				waf = 'Sucuri'

			elif 'Reblaze Secure Web Gateway' in str(x[1]) :
				waf = 'Reblaze'

			elif 'Server' in x[1].keys() and 'ECD' in x[1]['Server'] :
				waf = 'EdgeCast'

			elif 'Server' in x[1].keys() and 'NetDNA-cache' in x[1]['Server'] :
				waf = 'MaxCDN'

			if waf != '' :
				exit('~> {} detected in {}\n'.format(waf, link))

			else :
				exit('~> WAF not detected in {}\n'.format(link))

		else :
			exit('Your network connection is not stable\n')

	def start() :
		if len(argv) < 3 :
			exit('This function take 1 argument\n')

		else :
			scan(argv[2])

except KeyboardInterrupt :
	exit(' ~ Goodbye ;)\n')

except Exception :
	pass