"""Créer un tuple vide"""
tuple=tuple()
tuple=()

"""Créez un tuple contenant les noms de vos sœurs et de vos frères (les frères et sœurs imaginaires conviennent)"""
tuple_freres=('Fallou Fall','Mouhamed', 'Talla Fall', 'Khadim Fall')
tuple_soeurs=('Asta Fall', 'Diané Fall', 'Ndaye penda Fall', 'Mame Diarra Fall')

"""Rejoignez les tuples de frères et sœurs et attribuez-les aux frères et sœurs"""
tuple_freres_soeurs=tuple_soeurs+tuple_freres
print(tuple_freres_soeurs)

"""Combien de frères et sœurs avez-vous?"""
print(len(tuple_freres_soeurs))

"""Modifiez le tuple des frères et sœurs, ajoutez le nom de votre père et de votre mère et attribuez-le à family_members"""
family_members=list(tuple_freres_soeurs)
family_members.append('Ndaye Ami Der')
family_members.append('Ibrahima Fall')
print(family_members)

print("=============================================================================================================================================")

"""Décompressez les frères et sœurs et les parents de family_members"""
print(tuple_soeurs)
print(tuple_freres)
print(family_members)

"""Créez des tuples de fruits, légumes et produits d'origine animale. Joignez les trois tuples et affectez-les à une variable appelée food_stuff_tp."""
fruits=('Pomme', 'Orange', 'banane')
legumes=('Patate', 'Carrote', 'Oignon')
animal=('Mouton', 'chèvre', 'poulet')
food_stuff_tp=fruits+legumes+animal
print(food_stuff_tp)

"""Remplacez le tuple about food_stuff_tp par une liste food_stuff_lt"""
food_stuff_lt=list(food_stuff_tp)

"""Découpez le ou les éléments du milieu de la liste food_stuff_tp ou food_stuff_lt."""
decoupe_food_stuff_lt=food_stuff_lt[:4]
print(decoupe_food_stuff_lt)

"""Découpez les trois premiers éléments et les trois derniers éléments de la liste food_staff_lt"""
food_staff_lt_premier_element=food_stuff_lt[0:3]
food_staff_lt_dernier_element=food_stuff_lt[-4:-1]
print(food_staff_lt_premier_element)
print(food_staff_lt_dernier_element)

"""Supprimez complètement le tuple food_staff_tp"""
del food_stuff_lt

"""Vérifiez si un élément existe dans un tuple : Vérifiez si « l'Estonie » est un pays nordique"""
print('Estonie' in family_members)

"""Vérifiez si « l'Islande » est un pays nordique"""
print('Islande' in family_members)