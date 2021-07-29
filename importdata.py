import pandas
import csv

def importcells():
	'''
	Takes the station identifiers from the excel sheet and puts them into
	matrix form so that they can be used to automatically pull station data
	'''
	df = pandas.read_excel('usonly.xlsx', sheet_name = 'Sheet1')
	df.as_matrix()
	return df

def importtext(filename,usaf,wban):
	'''
	Attempt to make it easy to find the corresponding values in the data array. Doesn't work
	'''
	##	with open(filename,'r') as f:
	##		reader = csv.reader(f)
	##		output = list(reader)
	##		return output
	separator = ''.join([usaf,wban])
	df = pandas.read_csv(filename, sep=';' ,header=None, engine = 'python')
	return df.values
        
