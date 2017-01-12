# NIx GeoIP Tool
# nv 1.3
# Modulo Inicial

import mRouter

def header():
	hd = '\n'+'%44s'%'.__   __.  __  ___   ___\n'
	hd += '%44s'%'|  \ |  | |  | \  \ /  /\n'
	hd += '%44s'%'|   \|  | |  |  \  V  / \n'
	hd += '%44s'%'|  . `  | |  |   >   <  \n'
	hd += '%44s'%'|  |\   | |  |  /  .  \ \n'
	hd += '%51s'%'|__| \__| |__| /__/ \__\  nv1.3\n'
	print hd

def helper():
	hp = '\n'+'%44s'%'NIx Geo IP Tracking 1.0 (c) 2017 Lameck\n'
	hp += '%38s'%'https://github.com/lamecksf/nix/\n\n'
	hp += '%36s'%'usage: python nit.py [options]'

	hp += '\n\n'+'%51s'%'##########################################\n'
	hp += '%39s'%'SET IDENTIFIE PROTOCOL\n'
	hp += '%51s'%'##########################################\n\n'

	hp += '%40s'%'-i, --ip <iptarget or myip>%15s'%'Target IP\n\n'
	hp += '%30s'%'--all  %15s'%'All params\n'
	hp += '%30s'%'--status  %15s'%'Status\n'
	hp += '%30s'%'--country  %15s'%'Country\n'
	hp += '%30s'%'--country_code  %15s'%'Country Code\n'
	hp += '%30s'%'--region  %15s'%'Region\n'
	hp += '%30s'%'--city  %15s'%'City\n'
	hp += '%30s'%'--zipcode  %15s'%'Zipcode\n'
	hp += '%30s'%'--lat  %15s'%'Latitude\n'
	hp += '%30s'%'--lon  %15s'%'Longitude\n'
	hp += '%30s'%'--timezone  %15s'%'Timezone\n'
	hp += '%30s'%'--isp  %15s'%'ISP\n'
	hp += '%30s'%'--org  %15s'%'Organization\n'
	hp += '%30s'%'--as  %15s'%'As\n'
	hp += '%30s'%'--query  %15s'%'Identificate Protocol\n'
	hp += '%30s'%'--zpc  %15s'%'Postal Address System (Br)\n'
	hp += '\n\n'+'%35s'%'nit.py --ip myip --all --zpc\n'
	
	hp += '\n\n'+'%50s'%'##########################################\n'
	hp += '%35s'%'SET ZIPCODE\n'
	hp += '%50s'%'##########################################\n'
	
	hp += '\n'+'%30s'%'--gzip  %15s'%'Get Zipcode Area\n'
	hp += '%45s'%'country code >>>  %15s'%'Set code of country\n'
	hp += '%45s'%'zipcode >>>  %15s'%'Set zipecode of area\n'
	hp += '\n'+'%20s'%'nit.py --gzip \n'
	print hp

def gZip():
	print  ':: GET ZIP :: --------------------------------- \n\n'
	country_code = raw_input('%28s'%" country code >>> ")
	zipcode = raw_input('%28s'%" zipcode >>> ")
	print '\n'
	mRouter.setRote(country_code.strip(),zipcode.strip())
	