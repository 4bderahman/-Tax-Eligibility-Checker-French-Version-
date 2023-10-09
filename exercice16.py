age = int(input("Entrez l'âge de l'habitant : "))
sexe = input("Entrez le sexe de l'habitant (H pour homme, F pour femme) : ")

if (sexe == 'H' and age > 20) or (sexe == 'F' and age >= 18 and age <= 35):
    print("L'habitant est imposable.")
else:
    print("L'habitant n'est pas imposable.")
