

colwidths = [0,4,6,5,4,2,2,2,2,1,6,7,5,5,5,4,3,1,1,4,1,5,1,1,1,6,1,1,1,5,1,5,1,5,1]

impdata = {"USAF":2,"WBAN":3,"YR":4,"M":5,"D":6,"HR":7,"MIN":8,"LAT":10,"LONG":11,"ELEV - M":13,"WIND.DIR - DEGREES":16,
"WIND.SPD - M/S":19,"TEMP - CELSIUS, SCALE 10":29,"DEW.POINT - CELSIUS, SCALE 10":31,"ATM.PRES - HECTOPASCALS, SCALE 10":33}

def itemparse(data):
	dic = {}
	for identifier,num in impdata.items():
		tot = sum(colwidths[0:num])
		#print(sum(colwidths[0:num+1]))
		#print(identifier,num,data[tot:tot+colwidths[num]])
		dic.update({identifier: data[tot:tot+colwidths[num]]})
	print(dic)
