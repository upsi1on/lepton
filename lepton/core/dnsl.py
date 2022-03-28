try :
	import dns.resolver as dns
	import functions.basic as basic
	import socket
	import sys

	argv = sys.argv

	def start() :
		if len(argv) != 3 :
			exit('This function take 1 argument\n')

		url = basic.httporhttps(argv[2])

		if url :
			url = url[2].split('/')[0]

		else :
			url = argv[2].split('/')[0]

		try :
			ip = socket.gethostbyname(url)
			if ip != url :
				print('Host : {} ({})'.format(url, ip))

			else :
				print('Host : {}'.format(ip))

			print()

		except KeyboardInterrupt :
			exit(' ~ Goodbye ;)\n')

		except Exception :
			exit('Unable connect to {}\n'.format(repr(url)))

		else :
			tanya = False
			try :
				z = False
				for x in dns.query(url, 'TXT') :
					x = x.to_text()
					if not z :
						print('TXT :')
						z = True

					print('   {}'.format(x))
					tanya = True

			except KeyboardInterrupt :
				exit(' ~ Goodbye ;)\n')

			except Exception :
				pass


			try :
				z = False
				for x in dns.query(url, 'CNAME') :
					x = x.target
					if not z :
						print('CNAME :')
						z = True

					print('   {}'.format(x))
					tanya = True

			except KeyboardInterrupt :
				exit(' ~ Goodbye ;)\n')

			except Exception :
				pass


			try :
				z = False
				for x in dns.query(url, 'SOA') :
					x = x.to_text()
					if not z :
						print('SOA :')
						z = True

					print('   {}'.format(x))
					tanya = True

			except KeyboardInterrupt :
				exit(' ~ Goodbye ;)\n')

			except Exception :
				pass


			try :
				z = False
				for x in dns.query(url, 'MX') :
					x = x.to_text()
					if not z :
						print('MX :')
						z = True

					print('   {}'.format(x))
					tanya = True

			except KeyboardInterrupt :
				exit(' ~ Goodbye ;)\n')

			except Exception :
				pass


			try :
				z = False
				for x in dns.query(url, 'NS') :
					x = x.to_text()
					if not z :
						print('NS :')
						z = True

					print('   {}'.format(x))
					tanya = True

			except KeyboardInterrupt :
				exit(' ~ Goodbye ;)\n')

			except Exception :
				pass


			try :
				z = False
				for x in dns.query(url, 'PTR') :
					x = x.to_text()
					if not z :
						print('PTR :')
						z = True

					print('   {}'.format(x))
					tanya = True

			except KeyboardInterrupt :
				exit(' ~ Goodbye ;)\n')

			except Exception :
				pass


			try :
				z = False
				for x in dns.query(url, 'AAAA') :
					x = x.to_text()
					if not z :
						print('AAAA :')
						z = True

					print('   {}'.format(x))
					tanya = True

			except KeyboardInterrupt :
				exit(' ~ Goodbye ;)\n')

			except Exception :
				pass


			try :
				z = False
				for x in dns.query(url, 'A') :
					x = x.to_text()
					if not z :
						print('A :')
						z = True

					print('   {}'.format(x))
					tanya = True

			except KeyboardInterrupt :
				exit(' ~ Goodbye ;)\n')

			except Exception :
				pass

			if tanya :
				exit('\n~> Scanning complete, Success get DNS info\n')

			else :
				exit('~> Scanning complete, Failed get DNS info\n')

except KeyboardInterrupt :
	exit(' ~ Goodbye ;)\n')

except ModuleNotFoundError :
	exit('Install dnspython module!\n')

except Exception :
	pass