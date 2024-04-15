# sets
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]


""" EXERCICES: NIVEAU 1 """

"""Trouver la longueur de l'ensemble it_companies"""
print(len(it_companies))

"""Ajouter « Twitter » à it_companies"""
it_companies.add("Twitter")
print(it_companies)

"""Insérez plusieurs sociétés informatiques à la fois dans l'ensemble it_companies"""
it_companies.update(['whatsapp', 'Royaume', 'Volkeno'])
print(it_companies)

"""Supprimer une des sociétés de l'ensemble it_companies"""
it_companies.remove('Royaume')
print(it_companies)


"""EXERCICES: NIVEAU 2"""

"""Joindre A et B"""
C=A.union(B)
print(C)

"""Trouver une intersection B"""
print(A.intersection(B))

"""Est-ce qu'un sous-ensemble de B"""
print(A.issubset(B))

"""Les ensembles A et B sont-ils disjoints"""
print(A.isdisjoint(B))

"""Joindre A avec B et B avec A"""
print(A.union(B))
print(B.union(A))

"""Quelle est la différence symétrique entre A et B"""
print(A.symmetric_difference(B))

"""Supprimez complètement les ensembles"""
del A
del B


"""EXERCICES: NIVEAU 3"""

"""Convertissez les âges en un ensemble et comparez la longueur de la liste et de l'ensemble, lequel est le plus grand ?"""
set_age=set(age)
print(len(set_age))
print(len(age))
"""OUBIEN"""
def compare(age):
    if len( set_age)<len(age) :
        print(f"La liste age est plus grand que l'ensemble(set)")
    else:
        print(f"La liste age est plus petit que l'ensemble(set)")

compare_list_set=compare(age)

