#-*- conding: Utf-8 -*-

def tableMulti(base, debut, fin):
	print 'Fragment de la table de multiplication par', base, ':'
	n = debut
	while n <= fin:
		print n, ' x', base, ' =', n * base
		n = n +1