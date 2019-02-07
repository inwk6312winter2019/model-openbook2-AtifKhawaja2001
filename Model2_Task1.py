def street():
	l_strname = []
	l_fullname = []
	l_frmstreet = []
	l_tostreet = []
	l = []
	t = ()

	fout = open('Street_Centrelines.csv')
	for line in fout:
		line1 = line.split()
		l_strname.append(line1[2:3])
		l_fullname.append(line1[4:5])
		l_frmstreet.append(line1[6:7])
		l_tostreet.append(line1[7:8])


	t = zip(l_strname,l_fullname,l_frmstreet,l_tostreet)
	for string in t:
		l.append(string)
	print(l)

street()
