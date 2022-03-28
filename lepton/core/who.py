try :
	import whois
	import sys
	import functions.urlcheck
	import functions.basic
	import random
	import socket

	argv = sys.argv

	def start() :
		if len(argv) == 2 :
			exit('This function take 1 argument\n')

		while argv[2].endswith('/') :
			argv[2] = argv[2][:-1]

		if not functions.basic.httporhttps(argv[2]) :
			if not functions.urlcheck.start('https://{}'.format(argv[2].split('/')[0])) :
				argv[2] = 'http://' + argv[2].split('/')[0]

			else :
				argv[2] = 'https://' + argv[2].split('/')[0]

		if '/' in functions.basic.httporhttps(argv[2])[2] :
			argv[2] = functions.basic.httporhttps(argv[2])[0] + '://' + functions.basic.httporhttps(argv[2])[2].split('/')[0]

		if not functions.urlcheck.start(argv[2]) :
			exit('Unable connect to {}\n'.format(repr(functions.basic.httporhttps(argv[2])[2])))

		else :
			ip = socket.gethostbyname(functions.basic.httporhttps(argv[2])[2])
			if functions.basic.httporhttps(argv[2])[2] == ip :
				print('Host : {}\n'.format(ip))

			else :
				print('Host : {} ({})\n'.format(functions.basic.httporhttps(argv[2])[2], ip))

		try :
			output = whois.whois(argv[2])

		except KeyboardInterrupt :
			exit(' ~ Goodbye ;)\n')

		except socket.error as exc :
			logger.warning('Error trying to connect to socket: closing socket')

		if output :
			xyz = list(output.keys())
			nl = []
			apa = False
			while len(xyz) > 0 :
				c = random.choice(xyz)
				xyz.remove(c)
				if 'list' in str(type(output[c])) :
					if not apa :
						print('-' * 50)
						print()
						apa = True
					print('{} :'.format(c.replace('_', ' ')))
					for x in output[c] :
						print('   {}'.format(x))

					print()

				else :
					nl.append(c)

			while len(nl) > 0 :
				c = random.choice(nl)
				nl.remove(c)
				if output[c] != None :
					if not apa :
						print('-' * 50)
						print()
						apa = True
					print('{} : {}\n'.format(c.replace('_', ' '), output[c]))

			if apa :
				exit('~> Successfully to get whois information\n')

			else :
				exit('~> Failed to get whois info\n')

		else :
			exit('~> Failed to get whois info\n')

except KeyboardInterrupt :
	exit(' ~ Goodbye ;)\n')

except ModuleNotFoundError :
	exit('Install python-whois module!\n')

except Exception :
	pass