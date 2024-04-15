"""
Jour 2 : 30 jours de programmation python
"""

def main():
    # Déclarer une variable et lui affecter une valeur
    prenom = str('Magatte')
    nom = str('Fall')
    prenom_nom = str('Magatte Fall')
    pays = str('Sénégal')
    ville = str('Louga')
    age = int(22)
    annee = int(2024)
    is_married = bool(True)
    is_true = bool()

    # Déclarer plusieurs variables sur une même ligne
    prenom1, nom1, prenom_nom1, pays1, ville1, age1, annee1, is_married1, is_true1 = 'Anta', 'Fall', 'Anta fall', 'Sénégal', 'Thies', 22, 2024, True, True

    # Affichage de la longueur des variables à l'aide de la fonction len(),
    longueur = len(prenom)
    print("La logueur du prenom est :",longueur)

    nom = len(nom)
    print("La longueur du nom est",nom)

    prenom_nom = len(prenom_nom)
    print("La longueur du prenom et du nom est", prenom_nom)

    pays = len(pays)
    print("La longueur du pays est", pays)

    ville = len(ville)
    print("La longueur du ville est", ville)

    age = len( age)
    print("La longueur du  age est",  age)
if __name__ == '__main__':
    main()