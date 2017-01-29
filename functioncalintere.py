#-*- coding: Utf-8 -*-
#Script calculant les interé gagner sur un compte banquaire
#Autheur: MedaCorp

#Definition fonction
def calintere(sp,tf,ans):
    t = 1
    resultd = sp * tf / 100
    result = resultd + sp
    print t, "Annee. J ai", result, "sur mon compte epargne"
    while t < ans:
        t = t +1
        resultc = (result * tf / 100) + result
        result = resultc
        print t, "Annee. J ai", result, "sur mon compte epargne"
