import string

def read_file(file):
	fout = open(file)
	street(fout)
	print('\n')
	fout.seek(0)
	hist(fout)

def street(fout):
	l_strname = []
	l_fullname = []
	l_frmstreet = []
	l_tostreet = []
	l = []
	t = ()

	for line in fout:
		line1 = line.split(',')
		l_strname.extend(line1[2:3])
		l_fullname.extend(line1[4:5])
		l_frmstreet.extend(line1[6:7])
		l_tostreet.extend(line1[7:8])

	t = zip(l_strname,l_fullname,l_frmstreet,l_tostreet)
	for string in t:
		l.append(string)
	print("Result of subtask1 = ",l)

def hist(fout):
	d = {}
	l = []
	l_maint = []
	for line in fout:
		line1 = line.split(',')
		l_maint.append(line1[12:13])

#This code below breaks a list of lists into a single list
	for list in l_maint:
		for word in list:
			l.append(word)

#Dictionary of Maintenance as keys and total number of streets for each maintenance as values
	for key in l:
		d[key] = d.get(key,0) + 1
		val = d[key]
		d.setdefault(key,val)
	print("Dictionary of Maintenance = ",d)

read_file('Street_Centrelines.csv')
