def searchlongp(filename):
	f = open(filename, 'r')
	global txt
	global max
	global imax
	global longtxt
	txt = f.readlines()
	max = 0
	imax = 0
	i = 0
	lentxt = len(txt)
	longtxt = len(txt[i])
	while i <= lentxt:
		if longtxt > max:
			imax = txt[i]
			print i, len(txt), longtxt, max, imax, txt[i]
		i = i +1
		
	
	return txt[imax]
	f.close()
