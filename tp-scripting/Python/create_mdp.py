import random
import string

def create_mdp(length):
    """
    Créer une fonction qui génèreras un mot de passe d'une taille variable.

    Args:
        length : La longueur souhaitée du mot de passe.  

    Returns:
        str: Le mot de passe aléatoire généré.

    Usage : 
        Modifier la valeur de la variable passwd_size
        executer le script python3 create_mpd.py 

    """
    
    
    output = string.ascii_letters + string.digits + string.punctuation

    passwd = ''.join(random.choice(output) for _ in range(length))

    return passwd
    
# Modifier cette valeur pour changer la taille de votre mot de passe.
passwd_size = 40

passwd=create_mdp(passwd_size)

print(passwd)