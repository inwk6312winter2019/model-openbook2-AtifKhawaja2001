def bus_stops():
	l_location = []
	l_accessible = []
	l_strclass = []
	l = []
	l1 = []
	l2 = []
	l3 = []
	c = 0
	c1 = 0
	c2 = 0
	fout = open('Bus_Stops.csv')
	for line in fout:
		line1 = line.split(',')
		l_location.append(line1[6:7])
		l_accessible.append(line1[7:8])


	fin = open('Street_Centrelines.csv')
	for line in fin:
		line2 = line.split(',')
		l_strclass.append(line2[10:11])


	for i in range(len(l_location)):
		l.append(l_location[i])
		l.append(l_accessible[i])
		l.append(l_strclass[i])

#Accessible bus stops in Arterial roads
	for i in range(len(l)-2):
		if l[i+1] == ['Accessible']:
			if l[i+2] == ['ARTERIAL']:
				l1.append(l[i])
				c = c + 1

#Non-Standard bus stops in Local streets
	for i in range(len(l)-2):
		if l[i+1] == ['Non-Standard']:
			if l[i+2] == ['LOCAL STREET']:
				l2.append(l[i])
				c1 = c1 + 1

#Inaccessible bus stops in Minor Collectors
	for i in range(len(l)-2):
                if l[i+1] == ['Inaccessible']:
                        if l[i+2] == ['MINOR COLLECTOR']:
                                l3.append(l[i])
                                c2 = c2 + 1

	print(l1)
	print("Total number of Arterial bus stops = ",c,'\n')

	print(l2)
	print("Total number of Non-Standard Local Streets = ",c1,'\n')

	print(l3)
	print("Total number of Inaccessible bus stops in Minor Collectors = ",c2)


bus_stops()
