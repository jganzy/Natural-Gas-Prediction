import os
import requests
from contextlib import closing
import csv
import urllib.request
import datetime
import pandas
import getfile
import importdata
import parsedata


url="https://www1.ncdc.noaa.gov/pub/data/noaa/"

yearstart = 2010
yearend = 2010
#yearend = datetime.datetime.now().year

# usaf = str(723650)
# wban = str(23050)


#getfile.station.downloadfile(url,stations.stat1.usaf,stations.stat1.wban,yearstart,yearend)
#print(getfile.downloadfile.__doc__)

# for item in getfile.station._registry:
# 	getfile.station.downloadfile(url,item.usaf,item.wban,yearstart,yearend)
for i in range(yearstart, yearend+1):
	year = i
	col = importdata.importcells()
        
	for i in range(col.shape[0]):
		print(col['USAF'][i],col['WBAN'][i])
		usaf = str(col['USAF'][i])
                
		if len(str(col['WBAN'][i]))<5:
			wban = "0"+str(col['WBAN'][i])
		else:
			wban = str(col['WBAN'][i])

		downloadurl, filename, zipname = getfile.station.createurl(url,usaf,wban,year)
		getfile.station.downloadfile(downloadurl,filename,zipname)

		#need to find a way to sort the data and read here
		importedtext = importdata.importtext(filename, usaf, wban)
		print(importedtext[0][0])
		print(importedtext[1])
		parsedata.itemparse(importedtext[0][0])
		break
		if i>0:
			break
