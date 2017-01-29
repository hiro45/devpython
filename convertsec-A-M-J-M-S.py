nsd = input('Entree un nombre de secondes a convertire en Année, mois, jour, heure, minute et seconde. un grand nombre s impose !')

nspj = 3600 * 24 #Nombre de Secondes dans une journé

nspa = nspj * 365

nspm = nspj * 30

na = nsd / nspa
nsr = nsd % nspa

nmo = nsr / nspm
nsr = nsr % nspm

nj = nsr / nspj
nsr = nsr % nspj

nh = nsr / 3600
nsr = nsr % 3600

nmi = nsr / 60
nsr = nsr % 60

print "Nombre de secondes a convertir :", nsd
print "Cette duree correspond a", na, "annees de 365 jours, plus"
print nmo, "mois de 30 jours,",
print nj, "jours,",
print nh, "heures,",
print nmi, "minutes et",
print nsr, "secondes."
