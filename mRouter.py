# NIx GeoIP Tool
# nv 1.4
# Modulo Router

import mZPCBR
import mZPCUS

class Struct:
	def __init__(self):
		code = ''

country = Struct()
country.code = []

#++++++++++++++++++++++++++++++++++++++
country.code.append('br')
country.code.append('us')
country.code.append('')
#++++++++++++++++++++++++++++++++++++++

def setRote(countryCode,zipCode):

	if (countryCode.lower() == country.code[0]): # Brasil
		mZPCBR.zpcShoot(zipCode)
		mZPCBR.getDataPrint()

	if (countryCode.lower() == country.code[1]): # Units States
		mZPCUS.zpcShoot(zipCode)
		mZPCUS.getDataPrint()
	if (countryCode.lower() == country.code[2]): # 
		print '%38s'%'# :: NONE LIB TO THIS COUNTRY::\n'