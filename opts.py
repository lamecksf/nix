#Class
import json
import urllib2
import os

class Opts:

	
	def __init__(self):
		
		hd = '\n'+'%44s'%'.__   __.  __  ___   ___\n'
		hd += '%44s'%'|  \ |  | |  | \  \ /  /\n'
		hd += '%44s'%'|   \|  | |  |  \  V  / \n'
		hd += '%44s'%'|  . `  | |  |   >   <  \n'
		hd += '%44s'%'|  |\   | |  |  /  .  \ \n'
		hd += '%50s'%'|__| \__| |__| /__/ \__\  v1.0\n'
		self.head=hd
		
		helpp = '\n'+'%44s'%'NIx Geo IP Tracking 1.0 (c) 2017 Lameck\n'
		helpp += '%38s'%'https://github.com/lamecksf/nix/\n\n'
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


	
