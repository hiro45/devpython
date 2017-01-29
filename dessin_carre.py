#-*- coding:UTF-8 -*-

from dessin_tortue import *

up()								#relever le crayon
goto(0, 0)						#reculer en a gauche
speed("fast")

# dessiner dix carrés rouges aligné:
i = 0								#Compteur	
taillec = 25
taillet = 25
a = 30
while i <10:
	down()							#abaisser le crayon
	etoile5(taillet, 0, 'green')	#trace une etoila a 5 branche
	up()							#relever le crayon
	forward(a)						#avancer + loin
	down()							#abaisser le crayon
	triangle(taillet, 0, 'yellow')	#tracer un triangle
	up()							#relever le crayon
	forward(a)						#avancer + loin
	down()							#abaisser le crayon
	etoile6(taillet, 0, 'orange')	#trace une etoile a 6 branche
	up()							#relever le crayon
	forward(a)						#avancer + loin
	down()							#abaisser le crayon
	carre(taillec, 0, 'red')		#tracer un carré
	up()
	forward(a)
	down()
	
	i = i +1						#Incrementation compteur de 1 a chaque fois 
	taillec, taillet, a = taillec +5, taillet +5, a +5 #Incrementation des taille des triangle et des carre
a = input()							# attendre
