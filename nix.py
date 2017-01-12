#!/usr/bin/python
# NIx GeoIP Tool
# nv 1.3


import sys, getopt, os
import mInit, mIP
import mRouter

def main(argv):

	os.system("clear")
	mInit.header()

	try:
		opts, args = getopt.getopt(argv,'i:h', [
												'ip=',
												'all',
												'help',
												'status',
												'country',
												'country_code',
												'region',
												'city',
												'zipcode',
												'lat',
												'lon',
												'timezone',
												'isp',
												'org',
												'as',
												'query',
												'zpc',
												'gzip'])
	except getopt.GetoptError:
		print mIP.getTry()
		sys.exit(2)

	for opt, arg in opts:

		if opt in ('-h','--help'):
			mInit.helper()
			sys.exit()
		
		elif opt in ('-i', '--ip'):
			if arg == 'myip':
				ip = ''
			else:
				ip = arg
			mIP.geoIP(ip)

		elif opt in ('-a', '--all'):			
			mIP.getDataPrint()

		elif opt in ('--status'):
			print mIP.getStatus()

		elif opt in ('--country'):
			print mIP.getCountry()

		elif opt in ('--country_code'):
			print mIP.getCountryCode()

		elif opt in ('--region'):
			print mIP.getRegion()

		elif opt in ('--city'):
			print mIP.getCity()

		elif opt in ('--zipcode'):
			print mIP.getZip()

		elif opt in ('--lat'):
			print mIP.getLat()

		elif opt in ('--lon'):
			print mIP.getLon()

		elif opt in ('--timezone'):
			print mIP.getTimeZone()

		elif opt in ('--isp'):
			print mIP.getISP()

		elif opt in ('--org'):
			print mIP.getORG()

		elif opt in ('--as'):
			print mIP.getAs()

		elif opt in ('--query'):
			print mIP.getQuery()

		elif opt in ('--zpc'):
			mRouter.setRote(mIP.getCountryCode(),mIP.getZip())

		elif opt in ('--gzip'):
			mInit.gZip()
			


if __name__ == "__main__":
   main(sys.argv[1:])
