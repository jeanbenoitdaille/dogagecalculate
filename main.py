age = int(input("Entrez l'âge du chien: "))
 
if age < 0:
    print("Vous devez entrer un âge positif!")
    exit()
elif age <= 2:
    d_age = age * 10.5