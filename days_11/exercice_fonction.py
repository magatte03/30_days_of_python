"""
Declare a function add_two_numbers. It takes two parameters and it
returns a sum.
"""
#Déclarer une fonction
def add_two_numbers(number_one, number_two):
    return number_one+number_two
#Calling function
print(add_two_numbers(10,11))


"""
L'aire d'un cercle est calculée comme suit : aire = π xrx r. 
Écrivez une fonction qui calcule Area_of_circle
"""
#Déclarer fonction
def Area_of_circle(r):
    Pi=3.14
    return Pi*r*r
#Appeler la fonction
print(Area_of_circle(2))


"""
Écrivez une fonction appelée add_all_nums qui prend un nombre arbitraire 
d'arguments et additionne tous les arguments. Vérifiez si tous les éléments 
de la liste sont des types numériques. Sinon, donnez un retour raisonnable.
"""
#Déclarer
def add_all_nums(*args):
    total=0
    for arg in args:
        total+=arg
    return total 
#Appeler
print(add_all_nums(2,2,20))


"""
La température en °C peut être convertie en °F à l'aide de cette formule :
°F = (°C x 9/5) + 32. Écrivez une fonction qui convertit °C en °F, 
convert_celsius_to-fahrenheit .
"""
#Déclaration
def convert_celsius_to_fahrenheit(C):
    return (C * 9/5) + 32 
#Appeler
print(convert_celsius_to_fahrenheit(1))


"""
Écrivez une fonction appelée check-season, elle prend un paramètre de mois 
et renvoie la saison : Automne, Hiver, Printemps ou Été
"""
#Déclaration
def check_season(mois):
    if mois in ['janvier', 'octobre', 'novembre']:
        saison = "automne"
    elif mois in ['décembre', 'janvier', 'février']:
        saison = "Hiver"
    elif mois in ['mars', 'avril', 'mai']:
        saison = "printemps"
    elif mois in ['juin', 'juillet', 'août']:
        saison = "été"
    else:
        saison = "mois invalide"
    return saison
#Appeler
print(check_season('janvier'))


"""
Écrivez une fonction appelée calculate_slope qui renvoie la pente 
d'une équation linéaire
formule: y=ax+b
"""
#Déclaration
def calculate_slope(a, b):
    return a
#Appeler
print(calculate_slope(8,2))


"""
L'équation quadratique est calculée comme suit : ax² + bx + c = 0. 
Écrivez une fonction qui calcule l'ensemble de solutions d'une 
équation quadratique, solve_quadratic_eqn .
"""
#Déclaration
def solve_quadratic_eqn(a, b, c,x):
    return a*x**2 + b*x + c
#Appeler
print(solve_quadratic_eqn(2,1,1,3))


"""
Déclarez une fonction nommée print_list. Il prend une liste comme paramètre 
et imprime chaque élément de la liste.
"""
#Déclaration
def print_list(*list):
    listed=[]
    for listed in list:
        print(listed)
    return listed
#Appeler
print(print_list('décembre', 'janvier', 'février', 'novembre'))


"""
Déclarez une fonction nommée reverse_list. Il prend un tableau comme 
paramètre et renvoie l’inverse du tableau (utilisez des boucles).
"""
#Déclaration
def reverse_list(tab):
    return tab.reverse()
#Appeler
print(reverse_list(['1', '17', '4', '23']))


"""
Déclarez une fonction nommée capitalize_list_items. Il prend une liste 
comme paramètre et renvoie une liste d'éléments en majuscules
"""
#Déclaration
def capitalize_list_items(list):
    return [item.capitalize() for item in list]
# Appeler la fonction
print(capitalize_list_items(['éléments', 'prend', 'liste', 'fonction']))


"""
Déclarez une fonction nommée add_item. Il faut une liste et des paramètres 
d'élément. Il renvoie une liste avec l'élément ajouté à la fin.
"""
#Déclaration
def add_item(items, new_item):
    return items.append(new_item)
# Appeler la fonction
print(add_item(['éléments', 'prend'], 'paramètres'))


"""
Déclarez une fonction nommée remove_item. Il faut une liste et 
des paramètres d'élément. Il renvoie une liste avec l'élément supprimé.
"""
#Déclaration
def remove_item(items, item):
    return items.remove(item)
# Appeler la fonction
print(remove_item(['éléments', 'prend', 'paramètres'], 'paramètres'))


"""
Déclarez une fonction nommée sum_of_numbers. Il prend un paramètre numérique 
et ajoute tous les nombres de cette plage.
"""
#Déclaration
def sum_of_numbers(nums):
    return sum(nums)
# Appeler la fonction
print(sum_of_numbers(range(1, 5)))


"""
Déclarez une fonction nommée sum_of_odds. Il prend un paramètre numérique 
et ajoute tous les nombres impairs de cette plage.
"""
#Déclaration
def sum_of_odds(nums):
    return sum(num for num in nums if num % 2 != 0)
# Appeler la fonction
print(sum_of_odds(range(25)))


"""
Déclarez une fonction nommée sum_of_even. Il prend un paramètre numérique 
et ajoute tous les nombres pairs dans cette plage.
"""
#Déclaration
def sum_of_even(nums):
    return sum(num for num in nums if num % 2 == 0)
# Appeler la fonction
print(sum_of_even(range(25)))

"=========================== Exercices : niveau 2 =========================="
"""
Déclarez une fonction nommée evens_and_odds . Il prend un entier positif comme
paramètre et compte le nombre de pairs et d’impairs dans le nombre.
"""
#Déclaration
def evens_and_odds(number):
    evens = 0
    odds = 0
    # Convertir l'entier en une chaîne de caractères pour itérer sur chaque chiffre
    number_str = str(number)
    # Itérer sur chaque chiffre et compter les pairs et les impairs
    for digit in number_str:
        if int(digit) % 2 == 0:
            evens += 1
        else:
            odds += 1
    return evens, odds

# Appeler la fonction
print(evens_and_odds(1234567890))


"""
Appelez votre fonction factorielle, elle prend un nombre entier comme 
paramètre et renvoie une factorielle du nombre.
"""
#Déclaration
def factorielle(number):
    if number==1:
        return 1
    else:
        resultat=1
        for i in range(1, number+1):
            resultat*=i
        return resultat 
# Appeler la fonction
print(factorielle(8))


"""
Écrivez différentes fonctions qui prennent des listes. Ils doivent 
calculer_median
"""
def calcul_median(liste):
    """
    Calcule la médiane d'une liste de nombres.
    """
    sorted_list = sorted(liste)
    n = len(sorted_list)
    if n % 2 == 0:
        # Si le nombre d'éléments est pair, la médiane est la moyenne des deux éléments du milieu
        median = (sorted_list[n // 2 - 1] + sorted_list[n // 2]) / 2
    else:
        # Si le nombre d'éléments est impair, la médiane est l'élément du milieu
        median = sorted_list[n // 2]
    return median

# Exemple d'utilisation
liste1 = [1, 2, 3, 4, 5]
liste2 = [1, 2, 3, 4, 5, 6]
liste3 = [6, 2, 1, 9, 8, 3, 7, 5, 4]

print(calcul_median(liste1))  # Output: 3
print(calcul_median(liste2))  # Output: 3.5
print(calcul_median(liste3))  # Output: 5


"""
Écrivez différentes fonctions qui prennent des listes. Ils doivent 
calculate_mode
"""
def calcul_mode(liste):
    """
    Calcule le mode d'une liste de nombres.
    """
    # Création d'un dictionnaire pour stocker le nombre d'occurrences de chaque élément
    occurrences = {}
    for element in liste:
        if element in occurrences:
            occurrences[element] += 1
        else:
            occurrences[element] = 1
    
    # Recherche de l'élément avec le plus grand nombre d'occurrences
    mode = None
    max_occurrences = 0
    for element, occ in occurrences.items():
        if occ > max_occurrences:
            mode = element
            max_occurrences = occ
    
    return mode

# Exemple d'utilisation
liste1 = [1, 2, 2, 3, 3, 3, 4, 4, 5]
liste2 = [1, 2, 3, 4, 5]
liste3 = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5]

print(calcul_mode(liste1))  # Output: 3
print(calcul_mode(liste2))  # Output: 1 (ou n'importe quelle valeur unique dans la liste)
print(calcul_mode(liste3))  # Output: 1 et 2 (ou n'importe quelle valeur unique dans la liste)


"""
Écrivez différentes fonctions qui prennent des listes. Ils doivent 
calculer_range
"""
def calcul_range(liste):
    """
    Calcule l'étendue d'une liste de nombres.
    """
    if not liste:
        return None  # Si la liste est vide, l'étendue n'est pas définie
    return max(liste) - min(liste)

# Exemple d'utilisation
liste1 = [1, 2, 3, 4, 5]
liste2 = [-10, 0, 10, 20, 30]
liste3 = [5, 5, 5, 5, 5]

print(calcul_range(liste1))  # Output: 4 (5 - 1)
print(calcul_range(liste2))  # Output: 40 (30 - (-10))
print(calcul_range(liste3))  # Output: 0 (5 - 5)


"""
Écrivez différentes fonctions qui prennent des listes. Ils doivent 
calculate_variance
"""
def calcul_variance(liste):
    """
    Calcule la variance d'une liste de nombres.
    """
    if len(liste) == 0:
        return None  # Si la liste est vide, la variance n'est pas définie
    
    # Étape 1 : Calculer la moyenne
    moyenne = sum(liste) / len(liste)
    
    # Étape 2 : Calculer la somme des carrés des différences par rapport à la moyenne
    somme_carres_diff = sum((x - moyenne) ** 2 for x in liste)
    
    # Étape 3 : Calculer la moyenne des carrés des différences
    variance = somme_carres_diff / len(liste)
    
    return variance

# Exemple d'utilisation
liste = [2, 4, 4, 4, 5, 5, 7, 9]
print(calcul_variance(liste))  # Output: 4.0


"""
Écrivez différentes fonctions qui prennent des listes. Ils doivent 
calculate_écart_type
"""
import math

def calcul_ecart_type(liste):
    """
    Calcule l'écart type d'une liste de nombres.
    """
    # Étape 1 : Calculer la variance en utilisant la fonction précédente
    variance = calcul_variance(liste)
    
    if variance is None:
        return None  # Si la variance n'est pas définie, l'écart type n'est pas défini non plus
    
    # Étape 2 : Calculer l'écart type en prenant la racine carrée de la variance
    ecart_type = math.sqrt(variance)
    
    return ecart_type

# Exemple d'utilisation
liste = [2, 4, 4, 4, 5, 5, 7, 9]
print(calcul_ecart_type(liste))  # Output: 2.0



"""====================== Exercices : niveau 3 =============================="""
"""
Écrivez une fonction appelée is_prime, qui vérifie si un nombre est premier
"""
def is_prime(nombre):
    """
    Vérifie si un nombre est premier.
    """
    if nombre <= 1:
        return False  # Les nombres inférieurs ou égaux à 1 ne sont pas premiers
    
    # Vérifier si le nombre est divisible par un autre nombre que 1 et lui-même
    for i in range(2, int(nombre**0.5) + 1):
        if nombre % i == 0:
            return False  # Le nombre est divisible, donc il n'est pas premier
    
    return True  # Si aucun diviseur n'est trouvé, le nombre est premier

# Exemples d'utilisation
print(is_prime(5))   # Output: True
print(is_prime(16))  # Output: False
print(is_prime(23))  # Output: True
print(is_prime(1))   # Output: False
print(is_prime(0))   # Output: False

def sont_uniques(liste):
    """
    Vérifie si tous les éléments d'une liste sont uniques.
    """
    elements_vus = set()  # Utilisation d'un ensemble pour stocker les éléments vus
    
    for element in liste:
        if element in elements_vus:
            return False  # Si l'élément est déjà dans l'ensemble, il n'est pas unique
        else:
            elements_vus.add(element)  # Ajouter l'élément à l'ensemble
    
    return True  # Si aucun élément en double n'est trouvé, tous les éléments sont uniques

# Exemples d'utilisation
print(sont_uniques([1, 2, 3, 4, 5]))   # Output: True
print(sont_uniques([1, 2, 3, 4, 1]))   # Output: False (le 1 apparaît deux fois)
print(sont_uniques([]))                # Output: True (la liste vide a des éléments uniques)


"""
une fonction qui vérifie si tous les éléments de la liste sont du même
type de données
"""
def meme_type(liste):
    """
    Vérifie si tous les éléments d'une liste sont du même type de données.
    """
    if len(liste) == 0:
        return True  # Si la liste est vide, tous les éléments sont du même type (aucun)
    
    type_premier_element = type(liste[0])  # Récupérer le type du premier élément
    
    for element in liste[1:]:
        if type(element) != type_premier_element:
            return False  # Si le type de l'élément actuel est différent du type du premier élément, retourner False
    
    return True  # Si tous les types sont identiques, retourner True

# Exemples d'utilisation
print(meme_type([1, 2, 3, 4, 5]))    # Output: True (tous les éléments sont des entiers)
print(meme_type([1, 2.0, 3, 4, 5]))  # Output: False (int et float ne sont pas du même type)
print(meme_type([]))                 # Output: True (la liste vide a tous les éléments du même type)


"""
une fonction qui vérifie si la variable fournie est une variable python valide
"""
def est_variable_valide(variable):
    """
    Vérifie si la chaîne donnée est une variable Python valide.
    """
    return variable.isidentifier()

# Exemples d'utilisation
print(est_variable_valide("nom_variable"))    # Output: True
print(est_variable_valide("1variable"))       # Output: False (ne peut pas commencer par un chiffre)
print(est_variable_valide("_variable"))       # Output: True
print(est_variable_valide("variable_testée")) # Output: True


"""
Accédez au dossier data et accédez au fichier country-data.py.
Créez une fonction appelée les langues les plus parlées au monde. 
Il devrait renvoyer les 10 ou 20 langues les plus parlées dans le monde, 
par ordre décroissant.
Créez une fonction appelée most_populated_countries. Il devrait renvoyer 
10 ou 20 pays les plus peuplés par ordre décroissant.
"""
import os
import json

def les_langues_plus_parlees():
    """
    Renvoie les 10 ou 20 langues les plus parlées dans le monde par ordre décroissant.
    """
    # Chemin du fichier country-data.py
    chemin_fichier = os.path.join("data", "country-data.py")

    # Charger les données du fichier JSON
    with open(chemin_fichier, "r", encoding="utf-8") as f:
        data = json.load(f)
    
    # Extraire les langues et leurs nombres de locuteurs
    langues = data["langues"]
    
    # Trier les langues par nombre de locuteurs (dans l'ordre décroissant)
    langues_triees = sorted(langues.items(), key=lambda x: x[1], reverse=True)
    
    # Renvoyer les 10 ou 20 premières langues
    return langues_triees[:20] if len(langues_triees) > 20 else langues_triees

def pays_plus_peuples():
    """
    Renvoie les 10 ou 20 pays les plus peuplés par ordre décroissant.
    """
    # Chemin du fichier country-data.py
    chemin_fichier = os.path.join("data", "country-data.py")

    # Charger les données du fichier JSON
    with open(chemin_fichier, "r", encoding="utf-8") as f:
        data = json.load(f)
    
    # Extraire les pays et leur population
    pays = data["pays"]
    
    # Trier les pays par population (dans l'ordre décroissant)
    pays_tries = sorted(pays.items(), key=lambda x: x[1], reverse=True)
    
    # Renvoyer les 10 ou 20 premiers pays
    return pays_tries[:20] if len(pays_tries) > 20 else pays_tries

# Exemple d'utilisation
print("Les langues les plus parlées dans le monde :")
for langue, locuteurs in les_langues_plus_parlees():
    print(f"{langue} : {locuteurs}")

print("\nPays les plus peuplés dans le monde :")
for pays, population in pays_plus_peuples():
    print(f"{pays} : {population}")

