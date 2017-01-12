# NIx GeoIP Tool
# nv 1.3
# Modulo Router

import mZPC

class Struct:
	def __init__(self):
		code = ''

country = Struct()
country.code = []

#++++++++++++++++++++++++++++++++++++++
country.code.append('br')
country.code.append('us')
#++++++++++++++++++++++++++++++++++++++

def setRote(countryCode,zipCode):

	if (countryCode.lower() == country.code[0]): # Brasil
		mZPC.zpcShoot(zipCode)
		mZPC.getDataPrint()

	if (countryCode.lower() == country.code[1]): # Units States
		print '# :: NONE LIB TO THIS COUNTRY::'

