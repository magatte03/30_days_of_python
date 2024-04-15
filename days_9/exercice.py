"""
1)
Obtenez la contribution de l'utilisateur à l'aide de input (« Entrez votre âge : »). Si l'utilisateur a 18 ans ou plus,
donnez votre avis : vous êtes assez vieux pour conduire. S'il est inférieur à 18 ans, donnez votre avis pour attendre
 le nombre d'années manquant. Sortir:

 Enter your age: 30
You are old enough to learn to drive.
Output:
Enter your age: 15
You need 3 more years to learn to drive.
"""

age=int(input("Entrez votre âge :"))
if age>18:
    print("vous êtes assez vieux pour conduire")
elif age<18:
    age_sortant=18-age
    print(f"il vous manque {age_sortant} ans pour apprendre à conduire")
else:
    print("Vous avez 18ans, donc vous avez l'âge d'apprendre à conduire une voiture")

"======================================================================================================================="
"""
2)
Comparez les valeurs de my_age et your_age en utilisant if… else. Qui est le plus âgé (moi ou toi) ? Utilisez input
 ("Entrez votre âge :") pour obtenir l'âge en entrée. Vous pouvez utiliser une condition imbriquée pour imprimer
 « année » pour une différence d'âge d'un an, « années » pour des différences plus importantes et un texte personnalisé
 si mon_âge = votre_âge. Sortir:

 Enter your age: 30
You are 5 years older than me.
"""

my_age = 23
your_age = int(input("Entrez votre âge :"))
difference1 = my_age - your_age
difference2 = your_age - my_age

if your_age <= 0 or your_age >= 100:
    print("Ceci n'est pas un âge valide")
elif my_age < your_age:
    print(f"Vous êtes le plus âgé, vous avez {difference2} ans de plus que moi")
elif my_age > your_age:
    print(f"Je suis la plus âgée, j'ai {difference1} ans de plus que toi")
else:
    print("Nous avons le même âge")


"======================================================================================================================="
"""
3)
Obtenez deux numéros de l’utilisateur à l’aide de l’invite de saisie. Si a est supérieur à b, renvoie a est supérieur à 
b, si a est inférieur à b, renvoie a est plus petit que b, sinon a est égal à b. Sortir:

Enter number one: 4
Enter number two: 3
4 is greater than 3
"""

a = int(input("Entrer le premier nombre : "))
b = int(input("Entrer le deuxième nombre : "))

if a < b:
    print(f"le deuxieme nombre est plus grand")
elif a > b:
    print(f"le premier nombre est plus grand")
else:
    print("Nous avons le même nombre")


"============================================= ### Exercises: Level 2 =================================================="
"""
1)
Écrivez un code qui attribue une note aux étudiants en fonction de leurs scores :

80-100, A
70-89, B
60-69, C
50-59, D
0-49, F
"""
note = int(input("Entrer votre note: "))
if note <= 0 or note >= 101:
    print("Ceci n'est pas une note valide")
elif note<=0 or note<=49:
    print("F")
elif note==50 or note<=59:
    print("D")
elif note==60 or note<=69:
    print("C")
elif note==70 or note <= 79:
    print("B")
elif note==80 or note <= 100:
    print("A")


"======================================================================================================================="
"""
2)
Vérifiez si la saison est l'automne, l'hiver, le printemps ou l'été. Si la saisie de l'utilisateur est : septembre,
octobre ou novembre, la saison est l'automne. Décembre, janvier ou février, la saison est l'hiver. Mars, avril ou mai,
la saison est le printemps Juin, juillet ou août, la saison est l'été
"""

# Demander à l'utilisateur de saisir un mois
mois = input("Entrez un mois : ")

# Convertir le mois en minuscules pour éviter les problèmes de casse
mois = mois.lower()

# Vérifier si le mois appartient à l'automne
if mois in ['septembre', 'octobre', 'novembre']:
    saison = "automne"
# Vérifier si le mois appartient à l'hiver
elif mois in ['décembre', 'janvier', 'février']:
    saison = "hiver"
# Vérifier si le mois appartient au printemps
elif mois in ['mars', 'avril', 'mai']:
    saison = "printemps"
# Vérifier si le mois appartient à l'été
elif mois in ['juin', 'juillet', 'août']:
    saison = "été"
# Si le mois n'est pas valide, afficher un message d'erreur
else:
    saison = "mois invalide"

# Afficher la saison correspondante
print(f"La saison pour le mois de {mois} est {saison}.")


"======================================================================================================================="
"""
3)
La liste suivante contient quelques fruits :
fruits = ['banana', 'orange', 'mango', 'lemon']
Si un fruit n'existe pas dans la liste, ajoutez le fruit à la liste et imprimez la liste modifiée. Si le fruit existe,
print('Ce fruit existe déjà dans la liste')
"""

# Liste de fruits existants
fruits = ['banana', 'orange', 'mango', 'lemon']

# Demander à l'utilisateur de saisir un fruit
nouveau_fruit = input("Entrez un fruit : ")

# Vérifier si le fruit existe déjà dans la liste
if nouveau_fruit in fruits:
    print("Ce fruit existe déjà dans la liste.")
else:
    # Ajouter le nouveau fruit à la liste
    fruits.append(nouveau_fruit)
    print("Le fruit a été ajouté à la liste.")

# Afficher la liste mise à jour
print("Liste de fruits mise à jour :", fruits)


"=========================================== Exercices : niveau 3 ====================================================="
"""
Nous avons ici un dictionnaire de personnes. N'hésitez pas à le modifier !
*Vérifiez si le dictionnaire de la personne contient une clé de compétences. Si c'est le cas, imprimez la compétence
 intermédiaire dans la liste des compétences.
 *Vérifiez si le dictionnaire de la personne a une clé de compétences, si c'est le cas, vérifiez si la personne
 possède la compétence « Python » et imprimez le résultat.
*Si une personne possède uniquement des compétences JavaScript et React, print('Il est un développeur front-end'),
si la personne a des compétences Node, Python, MongoDB, print('Il est un développeur back-end'), si la personne a des
compétences React, Node et MongoDB, Print('Il est un développeur fullstack'), sinon print('titre inconnu') - pour des
résultats plus précis, davantage de conditions peuvent être imbriquées !
* Si la personne est mariée et vit en Finlande, imprimez les informations au format suivant :Asabeneh Yetayeh vit en Finlande. Il est marié.
"""
person = {
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_married': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
}

# Vérifier si le dictionnaire de la personne contient une clé de compétences
if 'skills' in person:
    # Imprimer la compétence intermédiaire dans la liste des compétences
    print('Compétence intermédiaire:', person['skills'][2])

    # Vérifier si la personne possède la compétence 'Python'
    if 'Python' in person['skills']:
        print('La personne possède la compétence Python.')
    else:
        print('La personne ne possède pas la compétence Python.')

    # Vérifier les compétences pour déterminer le titre
    if set(person['skills']) == {'JavaScript', 'React'}:
        print('Il est un développeur front-end.')
    elif set(person['skills']) == {'Node', 'Python', 'MongoDB'}:
        print('Il est un développeur back-end.')
    elif set(person['skills']) == {'React', 'Node', 'MongoDB'}:
        print('Il est un développeur fullstack.')
    else:
        print('Titre inconnu.')

    # Vérifier si la personne est mariée et vit en Finlande
    if person['is_married'] and person['country'] == 'Finland':
        print(f"{person['first_name']} {person['last_name']} vit en {person['country']}. Il est marié.")
