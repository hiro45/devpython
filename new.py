#-*- coding:UTF-8 -*-

from dessin_tortue import *

up()				#relever le crayon
goto(-150, 50)		#reculer en a gauche

# dessiner dix carrés rouges aligné:
i = 0
while i <10:
	down()				#abaisser le crayon
	carre(25, 'red')	#tracer un carré
	up()				#relevert le crayon
	forward(30)			#avancer + loin
	i = i +1
a = input()				# attendre