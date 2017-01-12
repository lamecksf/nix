# NIx GeoIP Tool
# nv 1.4
# Modulo Zipecode

import json
import urllib2

class Struct:
	def __init__(self):
		values = ''

s = Struct()
s.values = []

def zpcShoot(zipcode):
	response = urllib2.urlopen('http://api.zippopotam.us/us/'+zipcode)
	dt = response.read()
	dt_all = json.loads(dt)
	
	#SET ADDRESS ------------------------------
	s.values.append(dt_all['post code'])
	s.values.append(dt_all['country'])
	s.values.append(dt_all['country abbreviation'])
	s.values.append(dt_all['places'][0]['place name'])
	s.values.append(str(dt_all['places'][0]['longitude']))
	s.values.append(dt_all['places'][0]['state'])
	s.values.append(dt_all['places'][0]['state abbreviation'])
	s.values.append(str(dt_all['places'][0]['latitude']))
	#------------------------------------------
def getDataPrint():
	x = ':: ADDRESS US :: ------------------------------ \n\n'
	x += '|'+'%20s'%'Post Code  :: '+getPostCode()+'\n'
	x += '|'+'%20s'%'Country  :: '+getCountry()+'\n'
	x += '|'+'%20s'%'Country Code  :: '+getCountryCode()+'\n'
	x += '|'+'%20s'%'Place name  :: '+getPlaceName()+'\n'
	x += '|'+'%20s'%'Place lat  :: '+getPlaceLat()+'\n'
	x += '|'+'%20s'%'Place Lon  :: '+getPlaceLon()+'\n'
	x += '|'+'%20s'%'State Code  :: '+getStateCode()+'\n'
	x += '|'+'%20s'%'State  :: '+getState()+'\n'
	print x

def getPostCode():
	return s.values[0]
def getCountry():
	return s.values[1]
def getCountryCode():
	return s.values[2]
def getPlaceName():
	return s.values[3]
def getPlaceLat():
	return s.values[7]
def getPlaceLon():
	return s.values[4]
def getStateCode():
	return s.values[6]
def getState():
	return s.values[5]