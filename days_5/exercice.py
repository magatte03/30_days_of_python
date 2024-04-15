"""Déclarer une liste vide"""
#list=list()
#listes=[]

"""Déclarer une liste de plus de 5 éléments"""
list=('element1', 'element2', 'element3', 'element4', 'element5', 'element6')
print(list)
listes=['element1', 'element2', 'element3', 'element4', 'element5', 'element6', 'element7']
print(listes)

"""Trouvez la longueur de votre liste"""
print(len(list))

"""Obtenez le premier élément, l'élément du milieu et le dernier élément de la liste"""
print(list[0])
print(list[3])
print(list[-1])

"""Déclarez une liste appelée Mixed_data_types, mettez votre (nom, âge, taille, état civil, adresse)"""
Mixed_data_types = ['Magatte Fall', 22, 1.70, 'célibataire', 'Louga']

"""Déclarez une variable de liste nommée it_companies et attribuez les valeurs initiales Facebook, Google, Microsoft, Apple, IBM, Oracle et Amazon."""
it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']

"""Imprimez la liste en utilisant print()"""
print(it_companies)

"""Imprimer le nombre d'entreprises dans la liste"""
print(len(it_companies))

"""Imprimer la première, la deuxième et la dernière entreprise"""
print(it_companies[0])
print(it_companies[1])
print(it_companies[-1])

"""Imprimer la liste après avoir modifié une des sociétés"""
it_companies[0]='Tweeter'
print(it_companies)

"""Ajouter une société informatique à it_companies"""
it_companies.append('Samsung')
print(it_companies)

"Insérer une entreprise informatique au milieu de la liste des entreprises"
it_companies.insert(4, 'Lenovo')
print(it_companies)

"""Remplacez l'un des noms de it_companies en majuscules (IBM exclu !)"""
print(it_companies[4].swapcase())

"""Rejoignez les it_companies avec une chaîne '#; '"""


"""Vérifiez si une certaine entreprise existe dans la liste it_companies."""
est_present='Lenovo' in it_companies
print(est_present)

"""Trier la liste en utilisant la méthode sort()"""
it_companies.sort()
print(it_companies)

"""Inversez la liste par ordre décroissant en utilisant la méthode reverse()"""
it_companies.sort(reverse=True)
print(it_companies)

"""Supprimez les 3 premières entreprises de la liste"""
del it_companies[0:4]
print(it_companies)

"""Supprimez les 3 dernières entreprises de la liste"""
del it_companies[-4:]
print(it_companies)

"""Supprimez la ou les entreprises informatiques intermédiaires de la liste"""
it_companies.pop(0)
print(it_companies)

"""Supprimer la première entreprise informatique de la liste"""
#it_companies.pop(0)


"""les listes suivantes : """
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']

"""Rejoignez les listes """
rejoint_list = front_end + back_end
print(rejoint_list)

"""Copiez la liste jointe et attribuez-la à une variable full_stack"""
full_stack=rejoint_list.copy()
print(f"full_stack=",full_stack)

"""Insérez ensuite Python et SQL après Redux."""
full_stack.insert(5, 'Python')
print(full_stack)

full_stack.insert(6,'Redux')
print(full_stack)