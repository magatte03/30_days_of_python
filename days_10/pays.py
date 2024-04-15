pays = ["France", "Allemagne", "Espagne", "Italie", "Pays-Bas", "Royaume-Uni", "Suisse", "Canada", "États-Unis", "Australie", "Nouvelle-Zélande", "Algérie", "Maroc", "Tunisie", "Côte d'Ivoire", "Sénégal", "Burkina Faso", "Guinée", "Mali", "Tchad"]
pays_avec_terre = []
"""Parcourez les pays et extrayez tous les pays contenant le mot terr"""
for pays_nom in pays:
    if "terre" in pays_nom.lower():
        pays_avec_terre.append(pays_nom)

print("Les pays contenant le mot 'terre' sont :", pays_avec_terre)
print("===============================================================================================================")


"""Ceci est une liste de fruits, ['banane', 'orange', 'mangue', 'citron'] inversez l'ordre en utilisant une boucle."""
fruits= ['banane', 'orange', 'mangue', 'citron']
inverse=[]

for fruit in fruits:
    inverse.insert(0,fruit)

print("liste inversée:",inverse)
print("============================================================================================================")



