"""The following is a list of 10 students ages: """
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

"""Sort the list and find the min and max age"""
ages = sorted(ages,reverse=True)
print(ages)

print(ages[0])
print(ages[-1])

"""Trouvez l'âge médian (un élément du milieu ou deux éléments du milieu divisés par deux)"""
def age_median(ages):
    ages.sort()  # Tri de la liste d'âges
    n = len(ages)
    if n % 2 == 0:
        # Si le nombre d'éléments est pair
        median = (ages[n // 2 - 1] + ages[n // 2]) / 2
    else:
        # Si le nombre d'éléments est impair
        median = ages[n // 2]
    return median

# Exemple d'utilisation
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
print("Âge médian:", age_median(ages))

"""Trouver l'âge moyen (somme de tous les éléments divisée par leur nombre)"""
def age_moyen(ages):
    total_age = sum(ages)  # Somme de tous les âges
    nombre_personnes = len(ages)  # Nombre total d'éléments dans la liste
    moyenne = total_age / nombre_personnes
    return moyenne

# Exemple d'utilisation
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
print("Âge moyen:", age_moyen(ages))


"""Trouver la plage des âges (max moins min)"""
def plage_ages(ages):
    age_min = min(ages)  # Trouver l'âge le plus bas dans la liste
    age_max = max(ages)  # Trouver l'âge le plus élevé dans la liste
    plage = age_max - age_min
    return plage, age_max, age_min

# Exemple d'utilisation
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
print("Plage des âges, le maximum et le minimum:", plage_ages(ages))


"""Comparez la valeur de (min - moyenne) et (max - moyenne), utilisez la méthode abs()"""
def comparer_ecarts(ages):
    age_min = min(ages)  # Trouver l'âge le plus bas dans la liste
    age_max = max(ages)  # Trouver l'âge le plus élevé dans la liste
    age_moyen = sum(ages) / len(ages)  # Calculer l'âge moyen

    ecart_min = abs(age_min - age_moyen)  # Écart absolu entre l'âge minimum et l'âge moyen
    ecart_max = abs(age_max - age_moyen)  # Écart absolu entre l'âge maximum et l'âge moyen

    if ecart_min > ecart_max:
        print("L'écart entre l'âge minimum et l'âge moyen est plus grand.")
    elif ecart_max > ecart_min:
        print("L'écart entre l'âge maximum et l'âge moyen est plus grand.")
    else:
        print("Les écarts entre l'âge minimum et l'âge moyen, et entre l'âge maximum et l'âge moyen sont égaux.")

# Exemple d'utilisation
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
comparer_ecarts(ages)


"""Listes des pays"""
pays = [
'Afghanistan', 'Albania', 'Algeria', 'Andorra', 'Angola', 'Antigua and Barbuda', 'Argentina', 'Armenia', 'Australia', 'Austria'
]

"""Divisez la liste des pays en deux listes égales s'il n'y a même pas un pays de plus pour la première moitié."""
def diviser_liste_en_deux(liste):
    taille = len(liste)
    moitie = taille // 2

    if taille % 2 != 0:  # Si la taille de la liste est impaire
        moitie += 1  # Ajoute 1 pour que la première moitié ait un élément de plus

    liste_1 = liste[:moitie]  # Première moitié de la liste
    liste_2 = liste[moitie:]  # Deuxième moitié de la liste

    return liste_1, liste_2

# Exemple d'utilisation
liste_pays = ['Afghanistan', 'Albania', 'Algeria', 'Andorra', 'Angola', 'Antigua and Barbuda', 'Argentina', 'Armenia', 'Australia', 'Austria']
liste_1, liste_2 = diviser_liste_en_deux(liste_pays)
print("Première moitié :", liste_1)
print("Deuxième moitié :", liste_2)


"""Décompressez les trois premiers pays et le reste en tant que pays scandiques."""
def decompresser_pays(liste):
    trois_premiers_pays = liste[:3]  # Les trois premiers pays
    pays_scandinaves = liste[3:]  # Reste de la liste comme pays scandinaves
    return trois_premiers_pays, pays_scandinaves

# Exemple d'utilisation
liste_pays = ['Afghanistan', 'Albania', 'Algeria', 'Andorra', 'Angola', 'Antigua and Barbuda', 'Argentina', 'Armenia', 'Australia', 'Austria']
trois_premiers, scandinaves = decompresser_pays(liste_pays)
print("Trois premiers pays :", trois_premiers)
print("Pays scandinaves :", scandinaves)