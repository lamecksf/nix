# NIx GeoIP Tool
# nv 1.2
# Modulo Identifier Protocol

import json
import urllib2

class Struct:
	def __init__(self):
		values = ''

s = Struct()
s.values = []

def geoIP(ip):	
	response = urllib2.urlopen('http://ip-api.com/json/'+ip)
	dt = response.read()
	dt_all = json.loads(dt)
	#SET GEO IP------------------------------
	s.values.append(dt_all['status'])
	s.values.append(dt_all['country'])
	s.values.append(dt_all['countryCode'])
	s.values.append(dt_all['region'])
	s.values.append(dt_all['city'])
	s.values.append(dt_all['zip'])
	s.values.append(str(dt_all['lat']))
	s.values.append(str(dt_all['lon']))
	s.values.append(dt_all['timezone'])
	s.values.append(dt_all['isp'])
	s.values.append(dt_all['org'])
	s.values.append(dt_all['as'])
	s.values.append(dt_all['query'])
	#---------------------------------------

def getDataPrint():
	x = ':: GEO IP :: --------------------------------- \n\n'
	x += '|'+'%20s'%'Sucess :: '+getStatus()+'\n'
	x += '|'+'%20s'%'Country :: '+getCountry()+'\n'
	x += '|'+'%20s'%'Country Code :: '+getCountryCode()+'\n'
	x += '|'+'%20s'%'Region :: '+getRegion()+'\n'
	x += '|'+'%20s'%'City :: '+getCity()+'\n'
	x += '|'+'%20s'%'Zipcode :: '+getZip()+'\n'
	x += '|'+'%20s'%'Latitude :: '+getLat()+'\n'
	x += '|'+'%20s'%'Longitude :: '+getLon()+'\n'
	x += '|'+'%20s'%'TImezone :: '+getTimezone()+'\n'
	x += '|'+'%20s'%'ISP :: '+getISP()+'\n'
	x += '|'+'%20s'%'ORG :: '+getORG()+'\n'
	x += '|'+'%20s'%'AS :: '+getAS()+'\n'
	x += '|'+'%20s'%'Query :: '+getQuery()+'\n'
	print x

def getStatus():
	return s.values[0]
def getCountry():
	return s.values[1]
def getCountryCode():
	return s.values[2]
def getRegion():
	return s.values[3]
def getCity():
	return s.values[4]
def getZip():
	return s.values[5]
def getLat():
	return s.values[6]
def getLon():
	return s.values[7]
def getTimezone():
	return s.values[8]
def getISP():
	return s.values[9]
def getORG():
	return s.values[10]
def getAS():
	return s.values[11]
def getQuery():
	return s.values[12]
def getTry():
	return '%43s'%'try :: nit.py --ip myip\n'
