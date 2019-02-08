def read_file(file):
	fout = open(file)
	street(fout)
	print('\n')
	fout.seek(0)
	hist(fout)
	print('\n')
	fout.seek(0)
	own(fout)

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

#This code below combines a list of lists into a single list
	for list in l_maint:
		for word in list:
			l.append(word)

#Dictionary of Maintenance as keys and total number of streets for each maintenance as values
	for key in l:
		d[key] = d.get(key,0) + 1
		val = d[key]
		d.setdefault(key,val)
	print("Dictionary of Maintenance = ",d)


def own(fout):
	l_own = []
	l_strname = []
	l = []
	l1 = []
	l2 = []
	t = ()
	for line in fout:
		line1 = line.split(',')
		l_own.append(line1[11:12])
		l_strname.append(line1[4:5])

#This code below combines a list of lists into one list
	for list in l_own:
		for word in list:
			l.append(word)

	for list in l_strname:
		for word in list:
			l1.append(word)

#This code below creates a list of tuples where each tuple is a combinations of street name and its unique owner
	t = zip(l1,l)
	for pair in t:
		l2.append(pair)
	print("Street names and their unique owners = ",l2)

read_file('Street_Centrelines.csv')
