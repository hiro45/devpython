# Recherche d'un caractère particulier dans une chaîne
 
# Chaîne fournie au départ :
ch = input("Entre une chaine de caractere: ")
# Caractère à rechercher :
cr = input("Entree un caractere a rechercher dans la chaine: ")
# Recherche proprement dite :
lc = len(ch)    # nombre de caractères à tester
i = 0           # indice du caractère en cours d'examen
t = 0           # "drapeau" à lever si le caractère recherché est présent
cc = 0          # nombre de caractere compté dans la chaine ch
tt = 0
while i < lc:
    if ch[i] == cr:
        t = t +1
    i = i + 1
# Affichage :
print "Le caractère", cr,        
if t >= 1:
    print "est présent", t, "fois",
else:
    print "est inrouvable",
print "dans la chaîne:", ch  
