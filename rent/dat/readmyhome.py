with open("myhome",'r') as traindata:
	for data in traindata:
		if not len(data) or data.startswith("#"):
			continue
		distance, space, age,stair,aspect = map(str.strip,data.strip().split(','))
		print  map(str.strip,data.strip().split(','))

