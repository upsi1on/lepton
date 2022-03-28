try :
	import functions.basic
	import functions.getcontent
	import functions.urlcheck
	import socket
	import sys
	import queue
	import threading
	import re
	import socket

	argv = sys.argv
	q = queue.Queue()
	tab = False

	def start() :
		if len(argv) < 4 :
			exit('This function takes 2 arguments\n')

		else :
			if argv[2].upper() == 'PHP' :
				opend = open(functions.basic.pwd() + '/../asset/phpl', 'r')
				wl = opend.read().split('\n')
				opend.close()

			elif argv[2].upper() == 'ASP' :
				opend = open(functions.basic.pwd() + '/../asset/aspl', 'r')
				wl = opend.read().split('\n')
				opend.close()

			else :
				exit('{} programming language not supported\n'.format(argv[2]))

			pro = functions.basic.httporhttps(argv[3])
			if pro :
				link = pro[0] + '://' + pro[2].split('/')[0]

			else :
				if functions.urlcheck.start('http://' + argv[3].split('/')[0]) :
					link = 'http://' + argv[3].split('/')[0]

				elif functions.urlcheck.start('https://' + argv[3].split('/')[0]) :
					link = 'http://' + argv[3].split('/')[0]

				else :
					exit('Unable connect to {}\n'.format(repr(argv[3].replace('https://', '').replace('http://', ''))))

			if not functions.urlcheck.start(link) :
				exit('Unable connect to {}\n'.format(repr(link.replace('https://', '').replace('http://', ''))))

			else :
				for x in wl :
					q.put(x)

				def scan() :
					while not q.empty() :
						admin = q.get()
						try :
							dz = functions.getcontent.start(link + '/' + admin)
							if dz :
								global tab
								if not tab :
									tab = True
									print('Url with a checkmark, Indicates a login form\n' + '-' * 50)

								urlx = re.findall('type=[\'\"]password[\'\"]', dz[0].lower())
								if len(urlx) != 0 :
									print(link + '/' + admin + ' ✓')

								else :
									print(link + '/' + admin)

						except KeyboardInterrupt :
							exit(' ~ Goodbye ;)\n')

						finally :
							q.task_done()

				ip = socket.gethostbyname(link.replace('http://', '').replace('https://', ''))
				if link.replace('http://', '').replace('https://', '') == ip :
					print('Host : {}\n'.format(ip))

				else :
					print('Host : {} ({})\n'.format(link.replace('http://', '').replace('https://', ''), ip))

				for x in range(5) :
					t = threading.Thread(target = scan, daemon = True)
					t.start()

				q.join()
				exit('~> Scanning complete\n')

except KeyboardInterrupt :
	exit(' ~ Goodbye ;)\n')

except ModuleNotFoundError as e :
	exit(str(e)[17:-1] + ' module is needed\n')