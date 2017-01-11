#!/usr/bin/python
# NIx GeoIP Tool
# nv 1.1
#

import sys, getopt

from opts import Opts
from cIP import cIP

exp = Opts()
vIP = cIP()

def main(argv):

	print exp.getHead()

	try:
		opts, args = getopt.getopt(argv,'i:h', ['ip=','all','help','status','country','country_code','region','city','zipcode','lat','lon','timezone','isp','org','as','query'])
	except getopt.GetoptError:
		print vIP.getEr()
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
			vIP.ip = ip
			vIP.geoIP()

		elif opt in ('-a', '--all'):			
			print vIP.getDataPrint()

		elif opt in ('--status'):
			print vIP.getStatus()

		elif opt in ('--country'):
			print vIP.getCountry()

		elif opt in ('--country_code'):
			print vIP.getCountryCode()

		elif opt in ('--region'):
			print vIP.getRegion()

		elif opt in ('--city'):
			print vIP.getCity()

		elif opt in ('--zipcode'):
			print vIP.getZip()

		elif opt in ('--lat'):
			print vIP.getLat()

		elif opt in ('--lon'):
			print vIP.getLong()

		elif opt in ('--timezone'):
			print vIP.getTimeZone()

		elif opt in ('--isp'):
			print vIP.getISP()

		elif opt in ('--org'):
			print vIP.getORG()

		elif opt in ('--as'):
			print vIP.getAs()

		elif opt in ('--query'):
			print vIP.getQuery()



if __name__ == "__main__":
   main(sys.argv[1:])
