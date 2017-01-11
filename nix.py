#!/usr/bin/python
#
#
#

import sys, getopt
import popen2

from opts import Opts
exp = Opts()

def main(argv):

	print exp.getHead()

	try:
		opts, args = getopt.getopt(argv,'i:h', ['ip=','all','help','status','country','country_code','region','city','zipcode','lat','lon','timezone','isp','org','as','query','concat='])
	except getopt.GetoptError:
		print exp.getEr()
		sys.exit(2)

	for opt, arg in opts:

		if opt in ('-h','--help'):
			print exp.getHelp()
			sys.exit()
		
		elif opt in ('-i', '--ip'):
			if arg == 'myip':
				ip = ''
			else:
				ip = arg
			exp.ip = ip
			exp.geoIP()

		elif opt in ('-a', '--all'):			
			print exp.getDataPrint()

		elif opt in ('--status'):
			print exp.getStatus()

		elif opt in ('--country'):
			print exp.getCountry()

		elif opt in ('--country_code'):
			print exp.getCountryCode()

		elif opt in ('--region'):
			print exp.getRegion()

		elif opt in ('--city'):
			print exp.getCity()

		elif opt in ('--zipcode'):
			print exp.getZip()

		elif opt in ('--lat'):
			print exp.getLat()

		elif opt in ('--lon'):
			print exp.getLong()

		elif opt in ('--timezone'):
			print exp.getTimeZone()

		elif opt in ('--isp'):
			print exp.getISP()

		elif opt in ('--org'):
			print exp.getORG()

		elif opt in ('--as'):
			print exp.getAs()

		elif opt in ('--query'):
			print exp.getQuery()

		elif opt in ('--concat'):
			print arg




if __name__ == "__main__":
   main(sys.argv[1:])
