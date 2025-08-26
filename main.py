# La cible
import random


def verifie(cible, essai):
    if cible == essai:
        print("Bravo !!!")
        return 0
    elif cible < essai:
        print("Trop élevé...")
        return 1
    else:
        print("Trop peu...")
        return -1


prix_a_trouver = random.randint(1,10)
#print(f"Prix à trouver : {prix_a_trouver}")

for i in range(1, 6):

    # L'essai
    try:
        essai = input(f"Essai n°{i} : Votre proposition (entre 1 et 10) : ")
        essai = int(essai)
    except ValueError as err:
        print("Valeur incorrecte...")
        print(f"(Message du système : {err})")
        essai = -1 # pour éviter l'erreur en fin du "for" si aucune saisie est valide...
        continue

    # La comparaison
    if verifie(prix_a_trouver, essai) == 0:
            # Force la fin de la boucle
            break

if essai != prix_a_trouver:
    print("Perdu...")

print("Fin...")
