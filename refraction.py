import math

def loi_de_snell_descartes():
    n1 = float(input("Entrez l'indice de réfraction du rayon incident (n1) : "))
    n2 = float(input("Entrez l'indice de réfraction du rayon réfracté (n2) : "))
    theta_i = math.radians(float(input("Entrez l'angle d'incidence en degrés (θi) : ")))
    theta_r = math.degrees(math.asin(n1*math.sin(theta_i)/n2))
    print(f"L'angle de réfraction est de : {theta_r:.2f} degrés")

def vergence_lentille():
    lf = float(input("Entrez la longueur focale de la lentille en mètres : "))
    C = 1/lf
    print(f"La vergence de la lentille est de : {C:.2f} dioptries")

def equation_opticien():
    n = float(input("Entrez l'indice de réfraction de la lentille : "))
    R1 = float(input("Entrez le rayon de courbure de la première surface courbe rencontrée en mètres : "))
    R2 = float(input("Entrez le rayon de courbure de la deuxième surface courbe rencontrée en mètres : "))
    C = (n-1)*((1/R1)+(1/R2))
    print(f"La vergence de la lentille est de : {C:.2f} dioptries")

def vergence_systeme_lentilles():
    n_lentilles = int(input("Entrez le nombre de lentilles dans le système : "))
    vergences = []
    for i in range(n_lentilles):
        C_i = float(input(f"Entrez la vergence de la lentille {i+1} en dioptries : "))
        vergences.append(C_i)
    C_totale = sum(vergences)
    print(f"La vergence totale du système est de : {C_totale:.2f} dioptries")

print("Bienvenue dans le programme de calcul pour la réfraction !")
print("Voici les formules disponibles :")
print("1 - La loi de Snell-Descartes sur la réfraction")
print("2 - La vergence d'une lentille (C)")
print("3 - L'équation de l'opticien")
print("4 - La vergence d'un système de lentilles")

choix = int(input("Entrez le numéro de la formule que vous voulez utiliser : "))

if choix == 1:
    loi_de_snell_descartes()
elif choix == 2:
    vergence_lentille()
elif choix == 3:
    equation_opticien()
elif choix == 4:
    vergence_systeme_lentilles()
else:
    print("Choix invalide, veuillez réessayer.")
