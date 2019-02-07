import string

def street():
	l_strname = []
	l_fullname = []
	l_frmstreet = []
	l_tostreet = []
	l = []
	t = ()
	import string

	fout = open('Street_Centrelines.csv')
	for line in fout:
		line1 = line.split(',')
		#line2 = line.strip(string.punctuation + string.whitespace)
		l_strname.extend(line1[2:3])
		l_fullname.extend(line1[4:5])
		l_frmstreet.extend(line1[6:7])
		l_tostreet.extend(line1[7:8])


	#print(l_tostreet)
	t = zip(l_strname,l_fullname,l_frmstreet,l_tostreet)
	for string in t:
		l.append(string)
	print(l)

street()
