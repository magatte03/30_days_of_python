"""
Écrivez une fonction qui génère un random_user_id à six chiffres/caractères
"""


import random
import string

def generate_random_user_id(length=6):
    # Choix des caractères possibles pour l'ID utilisateur
    characters = string.ascii_letters + string.digits
    
    # Génération aléatoire de l'ID utilisateur
    random_user_id = ''.join(random.choice(characters) for i in range(length))
    
    return random_user_id

# Exemple d'utilisation de la fonction
random_id = generate_random_user_id()
print("Random User ID:", random_id)



"""
Modifiez la tâche précédente. Déclarez une fonction nommée user_id_gen_by_user.
Cela ne prend aucun paramètre mais prend deux entrées en utilisant input().
L'une des entrées est le nombre de caractères et la deuxième entrée est le 
nombre d'identifiants censés être générés.
"""


import random
import string

def user_id_gen_by_user():
    # Demander à l'utilisateur le nombre de caractères et le nombre d'identifiants à générer
    length = int(input("Entrez le nombre de caractères pour l'ID utilisateur : "))
    count = int(input("Entrez le nombre d'identifiants à générer : "))
    
    # Liste pour stocker les identifiants générés
    user_ids = []
    
    # Boucle pour générer le nombre spécifié d'identifiants
    for _ in range(count):
        # Génération aléatoire de l'ID utilisateur
        user_id = ''.join(random.choices(string.ascii_letters + string.digits, k=length))
        user_ids.append(user_id)
    
    return user_ids

# Exemple d'utilisation de la fonction
print(user_id_gen_by_user())
print(user_id_gen_by_user())


"""
Une fonction qui génére un mot de passe à un utilisateur 
"""

import random
import string

def generer_mot_de_passe(longueur):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    mot_de_passe = ''.join(random.choice(caracteres) for _ in range(longueur))
    return mot_de_passe

longueur_mot_de_passe = 12  # Spécifiez la longueur souhaitée du mot de passe
mot_de_passe_aleatoire = generer_mot_de_passe(longueur_mot_de_passe)
print("Mot de passe aléatoire:", mot_de_passe_aleatoire)



"""
Écrivez une fonction nommée rgb_color_gen. Il générera des couleurs RVB 
(3 valeurs allant de 0 à 255 chacune).
"""

import random

def rgb_color_gen():
    # Générer des valeurs RVB aléatoires entre 0 et 255 inclusivement
    red = random.randint(0, 255)
    green = random.randint(0, 255)
    blue = random.randint(0, 255)
    
    # Retourner les valeurs RVB sous forme de tuple
    return (red, green, blue)

# Exemple d'utilisation de la fonction rgb_color_gen
couleur = rgb_color_gen()
print("Couleur RVB générée:", couleur)


"========================= Exercices : niveau 2 ============================="
"""
Écrivez une fonction list_of_hexa_colors qui renvoie n'importe quel nombre de
couleurs hexadécimales dans un tableau (six nombres hexadécimaux écrits après
#. Le système numérique hexadécimal est composé de 16 symboles, 0-9 et les
6 premières lettres de l'alphabet, af. Vérifiez la tâche 6 pour exemples de 
sortie).
"""

import random

def list_of_hexa_colors(n):
    # Liste pour stocker les couleurs hexadécimales générées
    hex_colors = []

    # Générer n couleurs hexadécimales aléatoires
    for _ in range(n):
        # Générer chaque composante de couleur (6 caractères hexadécimaux)
        hex_color = '#' + ''.join(random.choices('0123456789abcdef', k=6))
        hex_colors.append(hex_color)

    return hex_colors

# Exemple d'utilisation de la fonction list_of_hexa_colors générant
# une liste de 5 couleurs hexadécimales aléatoires et les affichons.
nombre_de_couleurs = 5
couleurs_hexa = list_of_hexa_colors(nombre_de_couleurs)
print("Couleurs hexadécimales générées:", couleurs_hexa)


"""
Écrivez une fonction list_of_rgb_colors qui renvoie n'importe quel nombre
de couleurs RVB dans un tableau.
"""

import random

def list_of_rgb_colors(n):
    # Liste pour stocker les couleurs RVB générées
    rgb_colors = []

    # Générer n couleurs RVB aléatoires
    for _ in range(n):
        # Générer chaque composante de couleur RVB (valeurs entre 0 et 255)
        red = random.randint(0, 255)
        green = random.randint(0, 255)
        blue = random.randint(0, 255)
        
        # Ajouter la couleur RVB à la liste
        rgb_colors.append((red, green, blue))

    return rgb_colors

# Exemple d'utilisation de la fonction list_of_rgb_colors
nombre_de_couleurs = 5
couleurs_rgb = list_of_rgb_colors(nombre_de_couleurs)
print("Couleurs RVB générées:", couleurs_rgb)
 

"""
Écrivez une fonction generate_colors qui peut générer n'importe quel 
de couleurs hexa ou RVB.
"""

import random

def generate_colors(mode, n):
    colors = []
    if mode == 'hexa':
        for _ in range(n):
            hex_color = '#' + ''.join(random.choices('0123456789abcdef', k=6))
            colors.append(hex_color)
    elif mode == 'rgb':
        for _ in range(n):
            red = random.randint(0, 255)
            green = random.randint(0, 255)
            blue = random.randint(0, 255)
            rgb_color = f'rgb({red},{green},{blue})'
            colors.append(rgb_color)
    else:
        print("Mode non valide. Veuillez choisir 'hexa' ou 'rgb'.")

    return colors

# Exemples d'utilisation de la fonction generate_colors
print(generate_colors('hexa', 3)) # ['#a3e12f','#03ed55','#eb3d2b'] 
print(generate_colors('hexa', 1)) # ['#b334ef']
print(generate_colors('rgb', 3))  # ['rgb(5, 55, 175','rgb(50, 105, 100','rgb(15, 26, 80'] 
print(generate_colors('rgb', 1))  # ['rgb(33,79, 176)']


"========================== Exercices : niveau 3 ============================"
"""
Appelez votre fonction shuffle_list, elle prend une liste en paramètre et
renvoie une liste mélangée
"""

import random

def shuffle_list(input_list):
    shuffled_list = input_list[:]  # Créer une copie de la liste d'entrée
    random.shuffle(shuffled_list)  # Mélanger la copie de la liste
    return shuffled_list

# Exemple d'utilisation de la fonction shuffle_list
ma_liste = [1, 2, 3, 4, 5]
print("Liste originale:", ma_liste)
liste_melangee = shuffle_list(ma_liste)
print("Liste mélangée:", liste_melangee)


"""
Écrivez une fonction qui renvoie un tableau de sept nombres aléatoires compris entre 0 et 9. Tous les numéros doivent être uniques.
"""