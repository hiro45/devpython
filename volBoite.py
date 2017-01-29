#-*- coding: Utf-8 -*- 

##############################
##		Calcul Volume		##
##	        boite			##
##		 By Medacorp		##
##############################

#Definition function volboite qui calcule le volume d'une boite parallélipipédique
def volBoite(x1 =-1, x2 =-1, x3 =-1):
    "Volume d'une bo�te parall�lipip�dique"
    if x1 == -1 :
        return x1           # aucun argument n'a �t� fourni
    elif x2 == -1 :
        return x1**3        # un seul argument -> bo�te cubique
    elif x3 == -1 :
        return x1*x1*x2     # deux arguments -> bo�te prismatique
    else :
        return x1*x2*x3
