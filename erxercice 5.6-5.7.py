# Recherche d'un caract�re particulier dans une cha�ne
 
# Cha�ne fournie au d�part :
ch = input("Entre une chaine de caractere: ")
# Caract�re � rechercher :
cr = input("Entree un caractere a rechercher dans la chaine: ")
# Recherche proprement dite :
lc = len(ch)    # nombre de caract�res � tester
i = 0           # indice du caract�re en cours d'examen
t = 0           # "drapeau" � lever si le caract�re recherch� est pr�sent
cc = 0          # nombre de caractere compt� dans la chaine ch
tt = 0
while i < lc:
    if ch[i] == cr:
        t = t +1
    i = i + 1
# Affichage :
print "Le caract�re", cr,        
if t >= 1:
    print "est pr�sent", t, "fois",
else:
    print "est inrouvable",
print "dans la cha�ne:", ch  
