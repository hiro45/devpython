#-*- coding: Utf-8 -*-
#Script calculant les interé gagner sur un compte banquaire
#Autheur: MedaCorp

#Definition variable
spd = 2000			        										#Variable sp == Somme Placé au debart
tf = 1.75														    #Variable tf == Taux Fixe donné au debut de l'exercice
ans = 5															#Variable ans == les année ou nous avont laisser l'argent sans y toucher sur le compte
t = 1																#Variable t == compteur
resultd = spd * tf / 100												#Variable resultd == calcul des interé gagné
result = resultd + spd
print t, "Annee. J ai gagner", resultd, "donc maintenent j ai", result, "sur mon compte epargne"
while t < ans:
        t = t +1
        resultc = (result * tf / 100)
        resulti = resultc + result
        print t, "Annee. J ai gagner", resultc, "donc maintenent j ai", resulti, "sur mon compte epargne"
