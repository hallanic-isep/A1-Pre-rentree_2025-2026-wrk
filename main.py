# La cible
import random
prix_a_trouver = random.randint(1,10)
print(f"Prix à trouver : {prix_a_trouver}")

for i in range(1, 6):

    # L'essai
    essai = input(f"Essai n°{i} : Votre proposition (entre 1 et 10) : ")
    essai = int(essai)

    #print(f"Type de prix_a_trouver : {type(prix_a_trouver)}")
    #print(f"Type de essai : {type(essai)}")

    # La comparaison
    if prix_a_trouver == essai :
        print("Bravo !")
        break
    elif prix_a_trouver < essai :
        print("Trop élévé...")
    else:
        print("Trop peu...")

print("Fin...")