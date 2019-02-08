def bus():
	l_location = []
	l_accessible = []
	l_strclass = []
	l = []
	l1 = []
	c = 0
	fout = open('Bus_Stops.csv')
	for line in fout:
		line1 = line.split(',')
		l_location.append(line1[6:7])
		l_accessible.append(line1[7:8])
	#print(l_location)
	#print(l_accessible)

	fin = open('Street_Centrelines.csv')
	for line in fin:
		line2 = line.split(',')
		l_strclass.append(line2[10:11])
	#print(l_strclass)

	for i in range(len(l_location)):
		l.append(l_location[i])
		l.append(l_accessible[i])
		l.append(l_strclass[i])


	print(type(l[4]))
	for i in range(len(l)-2):
		if l[i+1] == ['Accessible']:
			if l[i+2] == ['ARTERIAL']:
				l1.append(l[i])
				c = c + 1
	print(l1)
	print("Total number of Arterial bus stops = ",c)

bus()
