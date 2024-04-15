def main():
    """Concatenate the string 'Thirty', 'Days', 'Of', 'Python'
    to a single string, 'Thirty Days Of Python'."""

    Thirty="Thirty"
    Days="Days"
    Of="Of"
    Python="Python"
    print(Thirty, Days, Of, Python)
    "==============================================================================="

    """Concatenate the string 'Coding', 'For' , 'All' to a single string, 'Coding For All'."""
    Coding="Coding"
    For="For"
    All="All"
    print(Coding,For,All)

    """Déclarez une variable nommée company et attribuez-lui une valeur initiale "Coding For All"."""
    company="Coding For All"

    """Imprimez la variable company en utilisant print()"""
    print(company)

    """Imprimez la longueur de la chaîne de l'entreprise en utilisant la méthode len() et print()"""
    print(len(company))

    """Changez tous les caractères en lettres majuscules à l’aide de la méthode upper()"""
    print(company.upper())

    """Changez tous les caractères en lettres minuscules en utilisant la méthode lower()"""
    print(company.lower())

    """Utilisez les méthodes capitalize(), title(), swapcase() pour formater la valeur de la chaîne Coding For All"""
    print(company.title())
    print(company.swapcase())
    print(company.capitalize())

    """Coupez (tranchez) le premier mot de la chaîne Coding For All """
    print(company.strip('Coding'))

    """Vérifiez si la chaîne Coding For All contient un mot Coding à l’aide de la méthode index, find ou d’autres méthodes."""
    print(company.find('Coding'))

    """Remplacez le mot coding dans la chaîne « Coding For All » par Python."""
    print(company.replace('Coding','Python'))

    """Remplacez Python pour tout le monde par Python pour tous à l'aide de la méthode de remplacement ou d'autres méthodes."""
    print(company.replace('Python For All', 'Python pour tous'))

    """Divisez la chaîne 'Coding For All' en utilisant l'espace comme séparateur (split()) ."""


if __name__ == '__main__':
    main()