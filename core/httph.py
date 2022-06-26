try :
	import socket
	import sys
	import functions.urlcheck
	import functions.getcontent
	import functions.basic

except KeyboardInterrupt :
	exit(' ~ Goodbye ;)\n')

except ModuleNotFoundError as e :
	exit(str(e)[17:-1] + ' module is needed\n')

try :
	argv = sys.argv

	def start() :
		if len(argv) == 2 :
			exit('This function take 1 argument\n')

		if not functions.basic.httporhttps(argv[2]) :

			ol = argv[2]

			if functions.urlcheck.start('https://' + argv[2]) :
				argv[2] = 'https://' + argv[2]

			else :
				argv[2] = 'http://' + argv[2]

		if not functions.urlcheck.start(argv[2]) :
			exit('Unable connect to ' + repr(ol) + '\n')

		res = functions.getcontent.start(argv[2])
		if len(str(res)) == 0 or res == False :
			print('Your network connection is not stable\n')

		else :
			if socket.gethostbyname(functions.basic.httporhttps(argv[2])[2].split('/')[0]) == functions.basic.httporhttps(argv[2])[2].split('/')[0] :
				print('Host : ' + functions.basic.httporhttps(argv[2])[2].split('/')[0])

			else :
				print('Host : ' + functions.basic.httporhttps(argv[2])[2].split('/')[0] + ' (' + socket.gethostbyname(functions.basic.httporhttps(argv[2])[2].split('/')[0]) + ')')

			z = 0
			print()
			for x in str(res[1]).split('\n') :
				if x != '' :
					print(' - ' + x)
					z += 1

			exit('~> ' + str(z) + ' data from http header\n')

except KeyboardInterrupt :
	exit(' ~ Goodbye ;)\n')