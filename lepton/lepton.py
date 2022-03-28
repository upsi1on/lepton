#!/usr/bin/python3
# coding: utf-8
try :
	print('╷      ┌────  ┌───╮  ──┬──  ╭───╮  ┌───╮\n│      ├────  ├───╯    │    │   │  │   │ By upsilonCrash\n└────  └────  ╵        ╵    ╰───╯  ╵   ╵\nThe author will not be responsible for your actions!\n')

	import sys

	if sys.version_info[0] != 3 :
		exit('Lepton is not compatible with python{}, Use python3!\n'.format(sys.version_info[0]))

	else :
		try :
			sys.dont_write_bytecode = True
			argv = sys.argv

			import ssl
			import core.httph
			import core.tcps
			import core.subs
			import core.crawl
			import core.waf
			import core.who
			import core.adminf
			import core.dnsl

		except ModuleNotFoundError as e :
			exit('Install {} module!\n'.format(str(e)[17:-1]))

		ssl._create_default_https_context = ssl._create_unverified_context

		if len(argv) == 1 :
			exit('Usage : python3 ' + repr(argv[0]) + ' { option } { host }\nOptions :\n   -t   TCP port scan           Example : [ -t 1,2,3 ][ -t 0-10 ][ -t 80 ][ -t ]\n   -s   Subdomain enumeration   Example : [ -s wordlist.txt ][ -s ]\n   -g   Get HTTP header\n   -i   Whois lookup\n   -a   Admin finder            Example : [ -a php ][ -a asp ]\n   -w   WEB crawling            Example : [ -w /save/to/directory/ ]\n   -f   WAF detection\n   -d   DNS lookup\n')

		elif argv[1].lower() == '-t' :
			core.tcps.start()

		elif argv[1].lower() == '-g' :
			core.httph.start()

		elif argv[1].lower() == '-s' :
			core.subs.start()

		elif argv[1].lower() == '-w' :
			core.crawl.start()

		elif argv[1].lower() == '-f' :
			core.waf.start()

		elif argv[1].lower() == '-a' :
			core.adminf.start()

		elif argv[1].lower() == '-i' :
			core.who.start()

		elif argv[1].lower() == '-d' :
			core.dnsl.start()

		else :
			exit('Unknown optional argument\n')

except KeyboardInterrupt :
	exit(' ~ Goodbye ;)\n')

except Exception :
	pass