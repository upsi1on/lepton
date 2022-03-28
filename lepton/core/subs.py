try :
	import socket
	import threading
	import queue
	import sys
	import functions.basic

except ModuleNotFoundError as e :
	exit(str(e)[17:-1] + ' module is needed\n')

q = queue.Queue()
count = 0
argv = sys.argv

def scan(host, lists) :
	for c in lists :
		q.put(c)

	def why() :
		while not q.empty() :
			sub = q.get()
			try :
				ip = socket.gethostbyname(sub + '.' + host)
			except :
				pass
			else :
				print(' - ' + sub + '.' + host + ' (' + ip + ')')
				global count
				count += 1
			q.task_done()

	if host.lower() != 'localhost' :
		for z in range(100) :
			t = threading.Thread(target = why, daemon = True)
			t.start()

	else :
		exit('~> 0 subdomain found\n')

	q.join()
	exit('~> ' + str(count) + ' subdomain found\n')

def start() :
	valid = False
	if len(argv) == 2 :
		exit('This function takes 1 - 2 arguments\n')

	elif len(argv) == 3 :
		c = 2

	else :
		c = 3

	if c == 3 :
		try :
			swl = open(argv[2])

		except :
			exit('File not found\n')

		file = ' '.join(swl.read().split('\n')).split()
		valid = True
		swl.close()

	else :
		files = open(functions.basic.pwd() + '/../asset/sub')
		file = files.read().split('\n')
		files.close()

	try :
		if '://' in argv[c] :
			socket.gethostbyname(argv[c].split('://')[1].split('/')[0])

		else :
			socket.gethostbyname(argv[c].split('/')[0])

	except :

		if '://' in argv[c] :
			exit('Unable connect to ' + repr(argv[c].split('://')[1].split('/')[0]) + '\n')

		else :
			exit('Unable connect to ' + repr(argv[c]) + '\n')

	else :

		if '://' in argv[c] :
			waifu = socket.gethostbyname(argv[c].split('://')[1].split('/')[0])
			if waifu == argv[c].split('://')[1].split('/')[0] :
				print('Host : ' + waifu + '\n')
			else :
				print('Host : ' + argv[c].split('://')[1].split('/')[0] + ' (' + waifu + ')\n')
			try :
				scan(argv[c].split('://')[1].split('/')[0], file)

			except KeyboardInterrupt :
				exit(' ~ Goodbye ;)\n')

		else :
			waifu = socket.gethostbyname(argv[c].split('/')[0])
			if waifu == argv[c].split('/')[0] :
				print('Host : ' + waifu + '\n')
			else :
				print('Host : ' + argv[c].split('/')[0] + ' (' + waifu + ')\n')
			try :
				scan(argv[c].split('/')[0], file)

			except KeyboardInterrupt :
				exit(' ~ Goodbye ;)\n')

	exit()