import os
import requests
from contextlib import closing
import csv
import urllib.request
import datetime
import getfile
import gzip
import shutil

class station:
	num_of_stats = 0
	total_population = 0
	_registry = []

	def __init__(self,usaf,wban,city,state,population):
		self.usaf = str(usaf)
		self.wban = str(wban)
		self.city = city
		self.state = state
		self.population = population
		station.num_of_stats += 1
		station.total_population += self.population
		self._registry.append(self)

	def createurl(url,usaf,wban,year):
		'''
		Creates URL download link for NOAA
		'''
		filename = "-".join([usaf,wban,str(year)])
		zipname = filename + ".gz"
		url_download = url + str(year) + "/" + zipname
		filename = ''.join([filename,".csv"])
		return  url_download, filename, zipname

	def downloadfile(url_download,filename,zipname):
		'''
		Downloads file from site. Extracts from zip and renames to csv
		'''
		urllib.request.urlretrieve(url_download,zipname)
		#with urlopen(image['url']) as in_stream, open(zipname, 'wb') as
		with gzip.open(zipname, 'rb') as f_in:
			with open(filename,'wb') as f_out:
				shutil.copyfileobj(f_in, f_out)
		os.remove(zipname)
