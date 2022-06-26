try :
	import socket
	import threading
	import struct
	import queue
	import sys
	import functions.basic

except Exception as e :
	exit(str(e)[17:-1] + ' module is needed\n')

q = queue.Queue()
argv = sys.argv
o = []
c = []
f = []

def scan(ip, port) :

	for x in port :
		q.put(x)

	def ha() :
		while not q.empty() :
			port = q.get()
			try :
				req = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
				req.setsockopt(socket.SOL_SOCKET, socket.SO_LINGER, struct.pack("ii", 1,0))
				req.settimeout(2)
				ret = req.connect_ex((ip, port))

				if ret == 0 :
					o.append(port)

				elif ret == 11 :
					f.append(port)

				else :
					c.append(port)

			except socket.timeout :
				f.append(port)

			except KeyboardInterrupt :
				exit(' ~ Goodbye ;)\n')

			finally :
				q.task_done()
				req.close()

	for x in range(100) :
		t = threading.Thread(target = ha, daemon = True)
		t.start()

	q.join()
	return [ o, f, c ]

def start() :
	if len(argv) == 2 :
		exit('This function takes 1 - 2 arguments\n')

	if len(argv) == 3 :
		c = 2

	else :
		c = 3

	if c == 2 :
		portx = open(functions.basic.pwd() + '/../asset/port')
		port = portx.read().split('\n')
		x = 0
		while x < len(port) :
			port[x] = int(port[x])
			x += 1
		portx.close()

	else :
		if ',' in argv[2] :
			arr = ' '.join(argv[2].split(',')).split()
			for port in arr :
				try :
					if int(port) > 65536 or int(port) < 0 :
						exit('Ports specified must be between 0 and 65535 inclusive\n')

				except ValueError :
					exit('Ports specified must be between 0 and 65535 inclusive\n')

			port = [int(x) for x in ' '.join(argv[2].split(',')).split()]

		elif '-' in argv[2] and argv[2].replace('-', '').isdigit() :
			ports = ' '.join(argv[2].split('-')).split()
			for port in ports :
				if not port.isdigit() :
					exit('Ports specified must be between 0 and 65535 inclusive\n')

			if str(argv[2])[0] == '-' :
				exit('Ports specified must be between 0 and 65535 inclusive\n')

			if argv[2].count('-') > 1 :
				a = ' '.join(argv[2].split('-')).split()
				argv[2] = str(a[0] + '-' + a[1])

			if int(argv[2].split('-')[0]) > int(argv[2].split('-')[1]) :
				exit('The first port must be smaller than the last port\n')

			if int(argv[2].split('-')[0]) > 65536 or int(argv[2].split('-')[1]) > 65536 :
				exit('Ports specified must be between 0 and 65535 inclusive\n')

			port = []
			x = int(ports[0])
			while x < int(ports[1]) + 1 :
				port.append(int(x))
				x += 1

		else :
			if not argv[2].isdigit() or int(argv[2]) > 65535 :
				exit('Ports specified must be between 0 and 65535 inclusive\n')
			port = [int(argv[2])]

	try :
		if '://' in argv[c] :
			argv[c] = argv[c].split('://')[1]

		if '/' in argv[c] :
			argv[c] = argv[c].split('/')[0]

		socket.gethostbyname(argv[c])

	except :
		try :
			exit('Unable connect to ' + repr(functions.basic.httporhttps(argv[c])[2].split('/')[0]) + '\n')

		except :
				exit('Unable connect to ' + repr(argv[c]) + '\n')

	else :
		p = functions.basic.httporhttps(argv[c])
		if not p :
			p = argv[c]

		else :
			p = p[2].split('/')[1]

		i = socket.gethostbyname(p)
		if p != i :
			print('Host : ' + p + ' (' + i + ')')

		else :
			print('Host : ' + p)

		try :
			port = scan(i, port)

		except KeyboardInterrupt :
			exit(' ~ Goodbye ;)\n')
		print('\nPort ' + ' ' * 7 + 'State' + ' ' * 7 + 'Service\n' + '-' * 44)
		if len(port[0]) != 0 :
			for x in port[0] :
				try :
					z = socket.getservbyport(x)
					if z == '' :
						z = 'unknown'

				except :
					z = 'unknown'
				print(str(x) + '/tcp' + ' ' * int(8 - len(str(x))) + 'open        ' + z)

		elif len(port[1]) < len(port[2]) and len(port[1]) != 0 or len(port[2]) == 0 :
			for x in port[1] :
				try :
					z = socket.getservbyport(x)
					if z == '' :
						z = 'unknown'

				except :
					z = 'unknown'
				print(str(x) + '/tcp' + ' ' * int(8 - len(str(x))) + 'filtered    ' + z)

		else :
			for x in port[2] :
				try :
					z = socket.getservbyport(x)
					if z == '' :
						z = 'unknown'

				except :
					z = 'unknown'
				print(str(x) + '/tcp' + ' ' * int(8 - len(str(x))) + 'close       ' + z)

		exit('~> ' + str(len(port[1])) + ' filtered / ' + str(len(port[2])) + ' close / ' + str(len(port[0])) + ' open\n')

	exit()