try :
	import re
	import os
	import sys
	import string
	import socket
	import random
	import functions.getcontent as nine
	import functions.urlcheck as iota
	import functions.basic as zero

	def start() :
		argv = sys.argv
		if len(argv) < 4 :
			exit('This function takes 2 arguments\n')

		pro = zero.httporhttps(argv[3])
		if pro :
			pro = pro[0]

		else :
			if iota.start('https://' + argv[3]) :
				pro = 'https'

			else :
				pro = 'http'

		url = pro + '://' + argv[3].replace('http://', '').replace('https://', '').split('/')[0]
		domain = argv[3].replace('http://', '').replace('https://', '').split('/')[0]

		def find(url) :
			listen = []
			while url.endswith('/') :
				url = url[:-1]
			res = nine.start(url)
			if res :
				if url.endswith('/sitemap.xml') :
					listen.extend(re.findall('<loc>(https:\/\/.+)<\/loc>', res[0]))
					listen.extend(re.findall('<loc>(http:\/\/.+)<\/loc>', res[0]))

				elif url.endswith('/robots.txt') :
					i = res[0].split('\n')
					for x in i :
						if x.startswith('Allow') :
							listen.append(x[6:].strip())

						if x.startswith('Disallow') :
							listen.append(x[9:].strip())

				else :
					listen.extend(re.findall("href=[\"\'](.*?)[\"\']", res[0]))
					listen.extend(re.findall("src=[\"\'](.*?)[\"\']", res[0]))

				internal = []
				eksternal = []

				for x in listen :
					while x.endswith('/') :
						x = x[:-1]

					if x.startswith('/') :
						x = x[1:]

					if x.startswith('https://') and x[8:].startswith(domain) :
						x = x[8:]

					if x.startswith('http://') and x[7:].startswith(domain) :
						x = x[7:]

					if x.startswith('www.') :
						x = x[4:]

					if not x.startswith('https://') and not x.startswith('http://') and not x.startswith(domain) :
						x = domain + '/' + x

					if x.startswith('https://') or x.startswith('http://') :
						eksternal.append(x)

					elif '?' in x  :
						bisa_berubah.append(x)

					else :
						internal.append(x)

				return [list(set(internal)), list(set(eksternal)), list(set(bisa_berubah))]

			else :
				return [[], [], []]

		if not os.path.isdir(argv[2]) :
			exit('Directory not found\n')

		if not iota.start(pro + '://' + argv[3].replace('http://', '').replace('https://', '')) :
			exit('Unable connect to {}\n'.format(repr(argv[3])))

		else :
			x = socket.gethostbyname(domain)
			if domain == x :
				print('Host : {}\n'.format(domain))

			else :
				print('Host : {} ({})\n'.format(domain, x))

			print('Please wait, This takes a lot of time . . .')

		hp = []
		eksternal = []
		bisa_berubah = []
		internal = []
		dibuka = [ domain + '/robots.txt', domain, domain + '/sitemap.xml' ]
		vurl = find(url)
		robot = find(url + '/robots.txt')
		sitemap = find(url + '/sitemap.xml')
		hp.extend(vurl[0])
		hp.extend(robot[0])
		hp.extend(sitemap[0])
		hp = list(set(hp))
		eksternal.extend(vurl[1])
		eksternal.extend(robot[1])
		eksternal.extend(sitemap[1])
		eksternal = list(set(eksternal))
		bisa_berubah.extend(vurl[2])

		def rangkak() :
			while True :
				x = random.choice(hp)
				hp.remove(x)
				if not x in dibuka :
					dibuka.append(x)
					z = find(pro + '://' + x)
					if not x in hp :
						hp.extend(z[0])
					eksternal.extend(z[1])
					internal.extend(z[0])
					bisa_berubah.extend(z[2])

				if len(hp) == 0 :

					ine = []
					for x in list(internal) :
						ine.append(x.split('#')[0])

					internal.clear()
					for x in ine :
						if x.endswith('/') :
							internal.append(x[:-1])

						else :
							internal.append(x)

					return [list(set(eksternal)), list(set(internal)), list(set(bisa_berubah))]

		x = rangkak()

		try :
			path = argv[2]
			if not path.endswith('/') :
				path = path + '/'

			try :

				os.makedirs(path + domain)

			except KeyboardInterrupt :
				exit(' ~ Goodbye ;)')

			except Exception :
				pass

			if len(x[1]) != 0 :
				tolol = []
				x[1].extend(robot[0])
				x[1].extend(vurl[0])
				x[1].extend(sitemap[0])
				x[1] = list(set(x[1]))
				for z in x[1] :
					tolol.append(pro + '://' + z)

				x[1] = tolol
				f = open(path + domain + '/internal.txt', 'w')
				f.write('\n'.join(x[1]))
				f.close()

			if len(x[0]) != 0 :
				x[0].extend(robot[1])
				x[0].extend(vurl[1])
				x[0].extend(sitemap[1])
				x[0] = list(set(x[0]))
				f = open(path + domain + '/external.txt', 'w')
				f.writelines('\n'.join(x[0]))
				f.close()

			if len(x[2]) != 0 :
				x[2].extend(robot[2])
				x[2].extend(vurl[2])
				x[2].extend(sitemap[2])
				x[2] = list(set(x[2]))
				gblk = []
				for z in x[2] :
					gblk.append(pro + '://' + z)

				x[2] = gblk
				f = open(path + domain + '/fuzzable.txt', 'w')
				f.write('\n'.join(x[2]))
				f.close()

		except KeyboardInterrupt :
			exit(' ~ Goodbye ;)\n')

		except Exception :
			exit('~> Crawl finished but failed to save result to directory :(\n')

		else :
			exit('~> Crawl finished, Sucess saving the result :)\n')

except KeyboardInterrupt :
	exit(' ~ Goodbye ;)\n')

except ModuleNotFoundError as e :
	exit(str(e)[17:-1] + ' module is needed\n')

except Exception :
	pass