# -*- coding: Utf-8 -*-
# Affichage des 50 premier terme de la table de 13
# avec signalement des multiples de 7

i = 1                       # compteur : prendra successivement les valeurs de 1 à 20
while i <51:
        # calcul du terme à afficher :
        t = i * 13
        # affichage sans saut à la ligne (utilisation de la virgule) :
        print t,
        # ce terme est-il un multiple de 3 ? (utilisation de l'opérateur modulo) :
        if t % 7 == 0:
            print "*",      # affichage d'une astérisque dans ce cas
        i = i +1            # incrémentation du compteur dans tous les cas
