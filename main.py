# La cible
import random
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
    if prix_a_trouver == essai :
        print("Bravo !")
        break
    elif prix_a_trouver < essai :
        print("Trop élévé...")
    else:
        print("Trop peu...")

print("Fin...")
