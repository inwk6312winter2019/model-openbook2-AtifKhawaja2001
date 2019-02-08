def bus_stops():
	l_location = []
	l_accessible = []
	l_strclass = []
	l_fdmbus = []
	l_fdmstr = []
	l1 = []
	l2 = []
	l3 = []
	l4 = []
	l5 = []
	c1 = 0
	c2 = 0
	c3 = 0
	fout = open('Bus_Stops.csv')
	for line in fout:
		line1 = line.split(',')
		l_location.append(line1[6:7])
		l_accessible.append(line1[7:8])
		l_fdmbus.append(line1[9:10])


	fin = open('Street_Centrelines.csv')
	for line in fin:
		line2 = line.split(',')
		l_strclass.append(line2[10:11])
		l_fdmstr.append(line2[23:24])


	for i in range(len(l_location)):
		l1.append(l_fdmbus[i])
		l1.append(l_location[i])
		l1.append(l_accessible[i])

	for i in range(len(l_strclass)):
		l2.append(l_fdmstr[i])
		l2.append(l_strclass[i])


	for i in range(1,len(l_location)):
		for j in range(1,len(l_strclass)):
			if l1[i] == l2[j]:
				if l1[i+2] == ['Accessible']:
					if l2[i+1] == ['ARTERIAL']:
						l3.append(l_location[i])
						c1 = c1 + 1
	for i in range(1,len(l_location)):
		for j in range(1,len(l_strclass)):
			if l1[i] == l2[j]:
				if l1[i+2] == ['Non-Standard']:
					if l2[i+1] == ['LOCAL STREET']:
						l4.append(l_location[i])
						c2 = c2 + 1

	for i in range(1,len(l_location)):
		for j in range(1,len(l_strclass)):
			if l1[i] == l2[j]:
				if l1[i+2] == ['Inaccessible']:
					if l2[i+1] == ['MINOR COLLECTOR']:
						l5.append(l_location[i])
						c3 = c3 + 1

	print(l3)
	print("Total number of bus stops that are Accessible and in Arterial roads = ",c1,'\n')

	print(l4)
	print("Total number of bus stops that are Non-Standard and in Local Streets = ",c2,'\n')

	print(l5)
	print("Total number of bus stops that are Inaccessible and in a Minor Collector = ",c3)

bus_stops()
