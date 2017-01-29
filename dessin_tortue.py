#-*- coding: Utf-8 -*-


from turtle import *


def carre(taille, angle, couleur):
	"fonction qui dessine un carr� de taille et de couleur détermine"
	color(couleur)
	left(angle)
	c = 0
	while c <4:
		forward(taille)
		right(90)
		c = c +1

def triangle(taille, angle, couleur):
	"fonction qui dessine un triangle de taille, angle et couleur determine"
	color(couleur)
	left(angle)
	c = 0
	while c <3:
		forward(taille)
		right(120)
		c = c +1
		
def etoile5(taille, angle, couleur):
	"fonction qui dessine une etoile a 5 branche"
	color(couleur)
	left(angle)
	c = 0
	while c <5:
		forward(taille)
		right(144)
		c = c +1
	
def etoile6(taille, angle, couleur):
	"fonction qui dessin une etoile a 6 branche avec la fonction triangle()"
	# declaration des variable
	color(couleur)
	left(angle)
	calfor1 = taille /3
	c = 0
	
	# boucle permetant de dessiné un triangle
	while c <1:
		triangle(taille, 0, couleur)
		c = c +1
	
	# 
	up()
	forward(calfor1)
	left(60)
	forward(calfor1)
	right(120)
	down()
	
	# boucle qui dessine le 2 triangle
	while c <2:
		triangle(taille, 0, couleur)
		c = c +1
