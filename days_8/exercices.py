"""Créez un dictionnaire vide appelé chien"""
chien={}

"""Ajoutez le nom, la couleur, la race, les pattes, l'âge au dictionnaire du chien"""
chien['nom']='Champion'
chien['couleur']='jaune'
chien['race']='rasologie'
chien['pattes']=4
chien['âge']='2ans'

"""Créez un dictionnaire étudiant et ajoutez le prénom, le nom, le sexe, l'âge, l'état civil, les compétences, 
le pays, la ville et l'adresse comme clés du dictionnaire."""
etudiant={'prénom':'Magatte', 'nom':'Fall', 'sexe':'Feminin', 'âge':22, 'état_civil':'Célibataire', 'compétences':'Développeuse web et mobile',
          'pays':'Sénégal', 'ville':'Louga', 'adresse':'villa 23'}

"""Obtenez la longueur du dictionnaire étudiant"""
print(len(etudiant))

"""Obtenez la valeur des compétences et vérifiez le type de données, cela devrait être une liste"""
print(etudiant['compétences'])

"""Modifier les valeurs des compétences en ajoutant une ou deux compétences"""
etudiant['compétences']='Gestion de projet'
print(etudiant['compétences'])

"""Obtenez les clés du dictionnaire sous forme de liste"""
cles=etudiant.keys()
print(cles)

"""Obtenez les valeurs du dictionnaire sous forme de liste"""
valeurs=etudiant.values()
print(valeurs)

"""Changez le dictionnaire en une liste de tuples à l'aide de la méthode items()"""
print(etudiant.items())

"""Supprimer un des éléments du dictionnaire"""
etudiant.pop('compétences')
del etudiant['adresse']

print(len(etudiant))

"""Supprimer l'un des dictionnaires"""
del chien

