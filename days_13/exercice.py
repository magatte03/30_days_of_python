"""
Filtrer uniquement les négatifs et les zéros dans la liste en utilisant 
la compréhension de liste
"""

numbers = [-4, -3, -2, -1, 0, 2, 4, 6]

# Utiliser la compréhension de liste pour filtrer les nombres négatifs et zéros
filtered_numbers = [num for num in numbers if num <= 0]

print(filtered_numbers)  #[-4, -3, -2, -1, 0]



"""
Aplatissez la liste de listes de listes suivante en une liste unidimensionnelle :
list_of_lists =[[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]
"""

list_of_lists = [[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]

# Utiliser une compréhension de liste imbriquée pour aplatir la liste de listes de listes
flattened_list = [num for sublist in list_of_lists for subsublist in sublist for num in subsublist]

print(flattened_list) #sortie: [1, 2, 3, 4, 5, 6, 7, 8, 9]


"""
En utilisant la compréhension de liste, créez la liste de tuples suivante :
[(0, 1, 0, 0, 0, 0, 0),
 (1, 1, 1, 1, 1, 1, 1),
 (2, 1, 2, 4, 8, 16, 32),
 (3, 1, 3, 9, 27, 81, 243),
 (4, 1, 4, 16, 64, 256, 1024),
 (5, 1, 5, 25, 125, 625, 3125),
 (6, 1, 6, 36, 216, 1296, 7776),
 (7, 1, 7, 49, 343, 2401, 16807),
 (8, 1, 8, 64, 512, 4096, 32768),
 (9, 1, 9, 81, 729, 6561, 59049),
 (10, 1, 10, 100, 1000, 10000, 100000)]
"""

# Utilisation d'une compréhension de liste pour générer la liste de tuples
list_of_tuples = [(i,) + tuple([j ** i for j in range(7)]) for i in range(11)]

print(list_of_tuples)


"""
Remplacez la liste suivante par une liste de dictionnaires :
sortie:
[{'country': 'FINLAND', 'city': 'HELSINKI'},
{'country': 'SWEDEN', 'city': 'STOCKHOLM'},
{'country': 'NORWAY', 'city': 'OSLO'}]
"""

countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]

# Utilisation d'une compréhension de liste pour créer la liste de dictionnaires
countries_dict = [{'country': country.upper(), 'city': city.capitalize()} for country, city in countries[0]]

print(countries_dict)


"""
Remplacez la liste de listes suivante par une liste de chaînes concaténées :
names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], 
[('Donald', 'Trump')], [('Bill', 'Gates')]]
sortie:
['Asabeneh Yetaeyeh', 'David Smith', 'Donald Trump', 'Bill Gates']
"""

names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]

# Utilisation d'une compréhension de liste pour créer la liste de chaînes concaténées
concatenated_names = [' '.join(name) for name in names]

print(concatenated_names)


"""
Écrivez une fonction lambda qui peut résoudre une pente ou une ordonnée à 
l'origine de fonctions linéaires.
"""

# Définition d'une fonction lambda pour résoudre la pente d'une fonction linéaire
slope = lambda x1, y1, x2, y2: (y2 - y1) / (x2 - x1)

# Définition d'une fonction lambda pour résoudre l'ordonnée à l'origine d'une fonction linéaire
# la fonction y_intercept pour calculer l'ordonnée à l'origine à partir de la pente, d'une 
# coordonnée x et d'une coordonnée y sur la ligne.
y_intercept = lambda slope, x, y: y - slope * x 
