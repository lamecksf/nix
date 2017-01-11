#Class
import json
import urllib2
import os
import popen2

class Opts():

	
	head 	= 	'\n'+'%44s'%'.__   __.  __  ___   ___\n'+'%44s'%'|  \ |  | |  | \  \ /  /\n'+'%44s'%'|   \|  | |  |  \  V  / \n'+'%44s'%'|  . `  | |  |   >   <  \n'+'%44s'%'|  |\   | |  |  /  .  \ \n'+'%50s'%'|__| \__| |__| /__/ \__\  v1.0\n'
	url 	= 	'http://ip-api.com/json/'
	er		=	'%43s'%'try :: nit.py --ip myip\n'
	ip 		=	''
	data	=	''

	


	def __init__(self,head=head,url=url,er=er):
		
		self.head=head
		self.url=url
		self.er=er

		helpp = '\n'+'%44s'%'NIx Geo IP Tracking 1.0 (c) 2017 Lameck\n'
		helpp += '%22s'%'https://github.com/lamecksf/nix/\n\n'
		helpp += '%36s'%'usage: python nit.py [options]\n\n'
		helpp += '%40s'%'-i, --ip <iptarget or myip>%15s'%'Target IP\n\n'
		helpp += '%30s'%'--all  %15s'%'All params\n'
		helpp += '%30s'%'--status  %15s'%'Status\n'
		helpp += '%30s'%'--country  %15s'%'Country\n'
		helpp += '%30s'%'--country_code  %15s'%'Country Code\n'
		helpp += '%30s'%'--region  %15s'%'Region\n'
		helpp += '%30s'%'--city  %15s'%'City\n'
		helpp += '%30s'%'--zipcode  %15s'%'Zipcode\n'
		helpp += '%30s'%'--lat  %15s'%'Latitude\n'
		helpp += '%30s'%'--lon  %15s'%'Longitude\n'
		helpp += '%30s'%'--timezone  %15s'%'Timezone\n'
		helpp += '%30s'%'--isp  %15s'%'ISP\n'
		helpp += '%30s'%'--org  %15s'%'Organization\n'
		helpp += '%30s'%'--as  %15s'%'As\n'
		helpp += '%30s'%'--query  %15s'%'Identificate Protocol\n'
		helpp += '\n\n'+'%30s'%'nit.py --ip myip --all\n'
		self.helpp=helpp


	# GETTERS ======================================================================================================

	def getHead(self):
		return self.head

	def getHelp(self):
		return self.helpp

	def getUrl(self):
		return self.url

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
		response = urllib2.urlopen(self.url+self.ip)
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

	def Concat(self,command):
		if( command.find('status') ):
			os.system(command+' '+self.getStatus())


