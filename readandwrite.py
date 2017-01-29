#-*- coding: Utf-8 -*-
# author Medacorp

#Scripte qui lit et ecrite dans un fichier text
# definition des fonction
def existef(filename):
	try:
		f = open(filename, 'r')
		f.close()
		return 1
	except:
		creatfi(filename)

def creatfi(filename):
	try:
		cf = raw_input("Voulez-vous cree se fichier ? Oui repondé 1 sinon reponder 0: ")
		if cf == 1:
			f = open(filename, 'w')
			f.close()
	except:
		print "Une erreur c'est produite"
		
def lectfichier(filename):
	f = open(filename, 'r')
	txt = f.readlines()
	i = 0
	while i < len(txt):
		print txt[i]
		i = i +1
	f.close()
	
def ecritfichier(filename):
	f = open(filename, 'a')
	espace = '\n'
	i = 1
	while i != 0:
		txt = raw_input("Entree le nouvelle lignes a ecrire dans le fichier:")
		if txt != '':
			f.write(txt + espace)
		else:
			print "Ecriture effectue avec succes !"
			i =  i -1
	
def changfichier(filename):
	filename = raw_input('Entree le nom du nouveau fichier: ')
	existef(filename)
	
def searchlongp(filename):
	f = open(filename, 'r')
	txt = f.readlines()
	max = 0
	imax = 0
	i = 0
	while i <= len(txt):
		if len(txt[i]) > max:
			max = len(txt[i])
			imax = i
			i = i +1
		else:
		i = i +1
	print "La phrase la plus long: ", txt[imax]
	f.close()

#Programme principale
#Definition des variable	
filename = raw_input("Entree le nom du fichier a cree ou a lire: ")
existef(filename)
txtt = "Au revoir !"
txte = "Il y as eu une erreur. Au revoir !"
i = 1

while i != 0:
	print 'Que voulez-vous faire ?\n 1: lire: ', filename, '\n 2: Ecrire de nouvelle lignes dans le fichier: ', filename, '? \n 3: Changer de fichier'
	print 'Entree 1, 2, 3, 4 ou laisse vide pour quitter: '
	choix = input()
	try:
		if choix == 1:
			lectfichier(filename)
		elif choix == 2:
			ecritfichier(filename)
		elif choix == 3:
			chnagfichier(filename)
		elif choix == 4:
			searchlongp(filename)
		else:
			print txtt
			i = i -1
	except:
		print txte
		i = i -1