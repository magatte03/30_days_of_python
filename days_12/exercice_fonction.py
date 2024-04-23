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