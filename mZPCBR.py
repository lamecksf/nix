# NIx GeoIP Tool
# nv 1.2
# Modulo Zipecode

import json
import urllib2

class Struct:
	def __init__(self):
		values = ''

s = Struct()
s.values = []

def zpcShoot(zipcode):
	response = urllib2.urlopen('http://cep.republicavirtual.com.br/web_cep.php?cep='+zipcode+'&formato=json')
	dt = response.read()
	dt_all = json.loads(dt)
	#SET ADDRESS ------------------------------
	s.values.append(dt_all['resultado_txt'])
	s.values.append(dt_all['resultado'])
	s.values.append(dt_all['logradouro'])
	s.values.append(dt_all['tipo_logradouro'])
	s.values.append(dt_all['bairro'])
	s.values.append(dt_all['cidade'])
	s.values.append(dt_all['uf'])
	#------------------------------------------

def getDataPrint():
	x = ':: ADDRESS BR :: ------------------------------ \n\n'
	x += '|'+'%20s'%'Sucess :: '+getStatus()+'\n'
	x += '|'+'%20s'%'Result :: '+getResult()+'\n'
	x += '|'+'%20s'%'Street :: '+getStreet()+'\n'
	x += '|'+'%20s'%'Type   :: '+getType()+'\n'
	x += '|'+'%20s'%'NeighborHood :: '+getNGBH()+'\n'
	x += '|'+'%20s'%'City :: '+getCity()+'\n'
	x += '|'+'%20s'%'COuntry Code :: '+getCountryCode()+'\n'
	print x

def getStatus():
	return s.values[0]
def getResult():
	return s.values[1]
def getStreet():
	return s.values[2]
def getType():
	return s.values[3]
def getNGBH():
	return s.values[4]
def getCity():
	return s.values[5]
def getCountryCode():
	return s.values[6]