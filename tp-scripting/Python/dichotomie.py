def dichotomie(tableau, element):
    """
    Créer une fonction qui tri un tableau.

    Args:
        tableau : un tableau de données
        element : un élément a "classer
        
    Returns:
    """
          
    debut = 0
    fin = len(tableau) - 1
    while debut <= fin:
        milieu = (debut + fin) // 2
        if tableau[milieu] < element:
            debut = milieu + 1
        elif tableau[milieu] > element:
            fin = milieu - 1
        else:
            return milieu
    tableau.insert(debut, element)
        
# Utilisation de la fonction pour générer un tableaux.

tableau=[]
add_number=""
while add_number != 0:
    add_number = int(input("Ajout d'un nouveau chiffre ou 0 pour quitter : "))
    dichotomie(tableau, add_number)
    print("Voici le tableau à jour : ", tableau, "\n")


