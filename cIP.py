#Class
import json
import urllib2
import os

class cIP:

	#ATTRIBUTS
	urlIP 	= 	'http://ip-api.com/json/'
	er		=	'%43s'%'try :: nit.py --ip myip\n'
	ip 		=	''
	data	=	''


	#CONSTRUCT
	def __init__(self,urlIP=urlIP,er=er):

		self.urlIP=urlIP
		self.er=er


	# GETTERS ======================================================================================================
	
	def getUrlIP(self):
		return self.urlIP

	def getEr(self):
		return self.er

	def getData(self):
		return self.data

	
	def getStatus(self):
		return self.status
	def getCountry(self):
		return self.country
	def getCountryCode(self):
		return self.countrycode
	def getRegion(self):
		return self.region
	def getCity(self):
		return self.city
	def getZip(self):
		return self.zip
	def getLat(self):
		return self.lat
	def getLong(self):
		return self.lon
	def getTimeZone(self):
		return self.timezone
	def getISP(self):
		return self.isp
	def getORG(self):
		return self.org
	def getAs(self):
		return self.ass
	def getQuery(self):
		return self.query
	
	def getDataPrint(self):		
		x = ':: GEO IP :: --------------------------------- \n\n'
		x += '|'+'%20s'%'Sucess :: '+self.getStatus()+'\n'
		x += '|'+'%20s'%'Country :: '+self.getCountry()+'\n'
		x += '|'+'%20s'%'Country Code :: '+self.getCountryCode()+'\n'
		x += '|'+'%20s'%'Region :: '+self.getRegion()+'\n'
		x += '|'+'%20s'%'City :: '+self.getCity()+'\n'
		x += '|'+'%20s'%'Zip Code :: '+self.getZip()+'\n'
		x += '|'+'%20s'%'Latitude :: '+self.getLat()+'\n'
		x += '|'+'%20s'%'Longitude :: '+self.getLong()+'\n'
		x += '|'+'%20s'%'TImezone :: '+self.getTimeZone()+'\n'
		x += '|'+'%20s'%'ISP :: '+self.getISP()+'\n'
		x += '|'+'%20s'%'ORG :: '+self.getORG()+'\n'
		x += '|'+'%20s'%'AS :: '+self.getAs()+'\n'
		x += '|'+'%20s'%'Query :: '+self.getQuery()+'\n'
		return x

	def __get__(self):
		return self.ip	
	#---------------------------------


	
	# SETTERS ========================================================================================================	
	
	def __set__(self):
		self.ip=ip.title()
	
		
	#++++++++++#
	#++++++++++#

	
	# METHODs  =======================================================================================================

	def geoIP(self):
		response = urllib2.urlopen(self.urlIP+self.ip)
		dt = response.read()
		dt_all = json.loads(dt)
		self.data = dt_all
		#SET-------------------------------------
		self.status 		=dt_all['status']
		self.country 		=dt_all['country']
		self.countrycode 	=dt_all['countryCode']
		self.region 		=dt_all['region']
		self.city 			=dt_all['city']
		self.zip 			=dt_all['zip']
		self.lat 			=str(dt_all['lat'])
		self.lon 			=str(dt_all['lon'])
		self.timezone 		=dt_all['timezone']
		self.isp 			=dt_all['isp']
		self.org 			=dt_all['org']
		self.ass 			=dt_all['as']
		self.query 			=dt_all['query']
		#---------------------------------------

	
