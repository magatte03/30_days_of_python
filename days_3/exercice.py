def main():
    # Déclarez votre âge sous forme de variable entière
    age = int(22)
    print(age)

    # Déclarez votre taille en tant que variable flottante
    taille = float(1.71)
    print(taille)

    # Déclarez une variable qui stocke un nombre complexe
    nombre_complexe = complex(2j)
    print(nombre_complexe)

    # Écrivez un script qui invite l'utilisateur à saisir la base et la hauteur du triangle et à calculer une aire de ce triangle (aire = 0,5 xbxh).
    base = int(input("Entrez la base du triangle: "))
    hauteur = int(input("Entrez la hauteur du triangle: "))
    aire = base * hauteur
    int_aire = int(aire)
    print(int_aire)

    #Écrivez un script qui invite l'utilisateur à saisir le côté a, le côté b et le côté c du triangle. Calculez le périmètre du triangle (périmètre = a + b + c)
    a = int(input("Enter side a: "))
    b = int(input("Enter side b: "))
    c = int(input("Enter side c: "))
    triangle = a + b + c
    print(triangle)

    #Obtenez la longueur et la largeur d'un rectangle à l'aide de l'invite. Calculer sa superficie (surface = longueur x largeur)
    #et son périmètre (périmètre = 2 x (longueur + largeur))
    length = int(input("enter length of a rectangle"))
    width = int(input("enter width of a rectangle"))
    area = length*width
    perimeter = 2 * (length + width)
    print("La surface:", area)
    print("Longueur est:", perimeter)

    #Obtenez le rayon d'un cercle à l'aide de l'invite. Calculez l'aire (aire = pi xrxr) et la circonférence (c = 2 x pi xr) où pi = 3,14.
    pi = 3, 14
    radius = int(input("enter the radius of a circle: "))
    area = pi * radius * radius
    circumference = 2 * pi * radius
    print("L'aire du cercle: ",area ,"La circonférence: ",circumference)

if __name__ == '__main__':
    main()