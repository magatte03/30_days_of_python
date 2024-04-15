"""============================================ Exercices : Niveau 1 =============================================="""
"""Itérez de 0 à 10 en utilisant la boucle for, faites de même en utilisant la boucle while."""
for number in range(11):
    print(number)

number=0
while number<11:
    print(number)
    number=number+1

"""Itérez de 10 à 0 en utilisant la boucle for, faites de même en utilisant la boucle while."""
for number in range(11,-1,-1):
    print(number)

number=11
while number>=0:
    print(number)
    number=number-1

"""Écrivez une boucle qui fait sept appels à print(), nous obtenons donc en sortie le triangle suivant"""
for i in range(8):
    print("#"*i)

print("========================================================================================================")

"""
Utilisez des boucles imbriquées pour créer les éléments suivants :
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
"""
for i in range(8):
    for n in range(8):
        print("#", end=" ")
    print()
print("========================================================================================================")

"""
Imprimez le motif suivant :
0 x 0 = 0
...   ...
9 x 9 = 81
10 x 10 = 100
"""
for i in range(11):
    resultat=i*i
    print(f"{i} x {i} = {resultat}")
print("============================================================================================================")


"""Parcourez la liste, ['Python', 'Numpy', 'Pandas', 'Django', 'Flask'] en utilisant une boucle for et imprimez les éléments"""
list=['Python', 'Numpy', 'Pandas', 'Django', 'Flask']
for i in list:
    print(i)
print("=============================================================================================================")


"""Utilisez la boucle for pour parcourir de 0 à 100 et imprimer uniquement les nombres pairs"""
for i in range(0,102,2):
    print(i)
print("==============================================================================================================")


"""Utilisez la boucle for pour parcourir de 0 à 100 et imprimer uniquement les nombres impairs"""
for i in range(1,102,2):
    print(i)
print("==============================================================================================================")


"""========================================== Exercices : niveau 2 =================================================="""
"""Utilisez la boucle for pour parcourir de 0 à 100 et imprimer la somme de tous les nombres."""
somme = (100 * (100 + 1)) // 2
print("La somme de tous les nombres est: ", somme)
print("==============================================================================================================")

"""Utilisez la boucle for pour parcourir de 0 à 100 et imprimer la somme de tous les pairs et la somme de toutes les cotes."""
somme_pairs=0
somme_impairs=0

for i in range(101):
    if i % 2 ==0:
        somme_pairs+=i
    else:
        somme_impairs+=i

print(f"La somme des nombres paires est : {somme_pairs}")
print(f"La somme des nombres impaires est : {somme_impairs}")
print("===============================================================================================================")


"""==========================================  Exercices : niveau 3 ================================================="""


