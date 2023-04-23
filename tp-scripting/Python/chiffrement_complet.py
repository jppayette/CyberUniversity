"""
Permet de jouer avec les fonctions d'encryption etc pour le TP - Scripting
"""

import random
import string
import sys, os
import base64
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

def encrypting_passwd(passwd):
    """Encrypte le mot de passe

    Args:
        passwd (str): mot de passe en clair

    Returns:
        set : la valeur du mot de passe encrypté ainsi que sa clef
    """
    key = Fernet.generate_key()
    f = Fernet(key)
    encrypted_passwd = f.encrypt(passwd.encode())    
    encrypted_passwd = {"encrypted_passwd":encrypted_passwd.decode(), "encrypted_key":key.decode()}
    return encrypted_passwd

def chiffrement(passwd):
    """
    
    chiffrement()  : chiffrer le mot de passe de la fonction create_mdp()
        Deux possibilité : 
            1 : chiffrer le mot de passe depuis la fonction create_mdp()
            2 : chiffrer un mot de passe depuis l'input de l'utilisateur    
            afficher 
                mot de passe chiffré
                cle de chiffrement
                
    Args :
        passwd (str): mot de passe en clair

             
    """
    os.system('clear')
    if passwd == None:
        passwd = input('Veuillez entrer un mot de passe a chiffrer : ')
        
    encrypted_passwd = encrypting_passwd(passwd)
    show_encrypted_passwd(encrypted_passwd)


def show_encrypted_passwd(encrypted_passwd):
    # os.system('clear')
    print("\n ============================================================================= \n")
    print("= Mot de passe chiffré : [", encrypted_passwd["encrypted_passwd"], "]")    
    print("= Clef de chiffrement : [", encrypted_passwd["encrypted_key"], "]")    
    print("\n WARNING : N'oubliez pas noter ces informations, elles ne sont pas conservées")
    print("\n =============================================================================")
    input("Press Enter to continue...")    
    main_menu()

def read_passwd():
    passwd = input("Veuillez entrer votre mot de passe a chiffrer : ")
    return passwd

def read_passwd_lenght():
    passwd_lenght = 0
    while passwd_lenght < 8:
        print("Quelle est la longueur du mot de passe souhaité ? (Min 8 charactères) : ")
        try:
            passwd_lenght=int(input())
            
            if passwd_lenght < 8:
                print("/!\ Désolé, vous devez avoir un minimum de 8 charactères.  Veuillez recommencer : \n")
        except ValueError:
            print("Ce nest pas un nombre")
    return passwd_lenght

def generate_passwd(passwd_lenght):
    output = string.ascii_letters + string.digits + string.punctuation
    passwd = ''.join(random.choice(output) for _ in range(passwd_lenght))
    return passwd

def show_passwd(passwd):
    os.system('clear')
    print("\n ============================================================================= \n")
    print("= Voici la valeur de votre mot de passe : [", passwd, "]")    
    print("\n WARNING : N'oubliez pas de le noter, il n'est pas conservé")
    print("\n =============================================================================")

def create_mdp():
    """    
    
    - create_mdp() : fonction de création d'un mot de passe en fonction de la taille choisis par l'utilisateur
        generer le mot de passe
        retourner la valeur du mot de passe
        afficher le mot de passe
    """
    os.system('clear')
    passwd_lenght = read_passwd_lenght()
    passwd = generate_passwd(passwd_lenght)
    show_passwd(passwd)
    encryption_dialog(passwd)

def encryption_dialog(passwd):
    """Chiffre un mot de passe 

    Args:
        passwd (_type_): _description_
    """
    chiffrer = input("\n Désirez vous le chiffrer? 'O'/'N' : ")  
    
    if chiffrer == 'O':
        chiffrement(passwd)

    else:
        print("Retour au menu principal!")
        main_menu()

def dechiffrement():
    """
    dechiffrement() : permettre de dechiffrer le mot de passe de la fonction chiffrement()
        Déchiffrer le mot de passe en ayant en input
            mot de passe chiffré
            clef de chiffrement
    
    """
    os.system('clear')
    encrypted_data = read_decrypt_passwd_dialog()
    passwd = decrypt_passwd(encrypted_data)
    show_passwd(passwd["decrypt_passwd"])

def decrypt_passwd(encrypted_data):
    """Déchiffre le mot de passe

    Args:
        encrypted_data (set): Les données chiffrés

    Returns:
        set: Les données déchiffrés
    """
    key = encrypted_data["encrypted_key"]
    print(key)
    f = Fernet(key)
    decrypt_passwd = f.decrypt(encrypted_data["encrypted_passwd"].encode())
    decrypt_passwd={"decrypt_passwd":decrypt_passwd.decode()}
    return decrypt_passwd
    
def read_decrypt_passwd_dialog():
    """Boite de dialogue de lecture des mots de passes pour le déchiffrement

    Returns:
        set: contient les données mot de passe chiffré et clé de déchiffrement
    """
    encrypted_passwd  = input("Quel est le mot de passe encrypté? (base64) : " )
    encrypted_key = input("Quel est la clef d'encryption? : ")
    encrypted_data = {"encrypted_passwd":encrypted_passwd,"encrypted_key":encrypted_key}
    return encrypted_data

def read_mp():
    """
    - read_mdp() : lire le mot de passe depuis le fichier spécifié par l'utilisateur
        Lecture du nom du fichier
        Chiffrement du mot de passe
        afficher 
            mot de passe chiffré
            cle de chiffrement
            
            
    Fonction globale de lecture du mot de passe 
    """
    os.system('clear')
    passwd = read_file()
    show_passwd(passwd)
    encryption_dialog(passwd)

def read_file():
    """ Demande quel est le fichier à ouvrir
    """
    os.system('clear')
    filename = input('Quel est le nom du fichier à ouvrir ? : ')
    with open(filename, "r") as f:
       passwd = f.readline().split()[0]
    return(passwd)

def encrypt_dialog():
    """ Boite de dialogue pour chiffrer un message avec mot de passe

    Returns:
        _type_: _description_
    """
    os.system("clear")
    message = input('Quel message désirez-vous chiffrer  ? : ').encode()
    password = input('Que est le mot de passe correspondant ? : ').encode()

    # salt = os.urandom(16)
    # Dans le cas actuel, ce salt est en dur dans le fichier, 
    # Accessoirement, il pourrait être disponible sur un serveur distant.
    salt = b'*\x10\xb1\xe1\xc6\xd9\x84\x9ba\r\xe0W\xa3\xd8\xa9\x11'
    
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=480000,
    )

    key = base64.urlsafe_b64encode(kdf.derive(password))
    
    f = Fernet(key)
    
    encrypted_passwd = f.encrypt(message)
    encrypted_passwd = {"encrypted_passwd":encrypted_passwd ,"encrypted_key": key}
    return encrypted_passwd


def decrypt_dialog():
    """ Boite de dialogue pour entrer quelles sont les messages  / mot de passe utilisateur

    Returns:
        _type_: _description_
    """
    message = input('Quel message désirez-vous dechiffrer  ? : ').encode()
    password = input('Que est le mot de passe correspondant ? : ').encode()
    
    salt = b'*\x10\xb1\xe1\xc6\xd9\x84\x9ba\r\xe0W\xa3\xd8\xa9\x11'
            
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=480000,
    )

    key = base64.urlsafe_b64encode(kdf.derive(password))
    f = Fernet(key)
    decrypted_message = f.decrypt(message)
    return decrypted_message.decode()


def encrypt_message():
    """ Chiffre une chaine de caractere avec un mot de passe fourni par l'utilisateur
    """
    encrypted_passwd = encrypt_dialog()
    show_encrypted_passwd(encrypted_passwd)


def decrypt_message():
    """ Déchiffre une chaine de caractere avec un mot de passe fourni par l'utilisateur
    """
    passwd = decrypt_dialog()
    show_passwd(passwd)
    
















def main_menu():
    """ Menu de selection
    
    """

    print("=============================================================================\n")
    print("Faites une sélection : \n ")

    print(" 1 ) Créer un mot de passe : ")
    print(" 2 ) Chiffrer un mot de passe : ")
    print(" 3 ) Déchiffrer un mot de passe : ")
    print(" 4 ) Lire un mot de passe depuis un fichier : ")
    print(" 5 ) Chiffrer un message avec un mot de passe") 
    print(" 6 ) Déhiffrer un message avec un mot de passe") 
    
    print(" Q ) Quitter le program : ")

    print("\n ---------- \n ")

    choice = input("Selectionner une option : ")


    match choice:
        case "1":
            print('value 1')
            create_mdp()
            
        case "2":
            print('value 2')
            chiffrement(passwd=None)
            
        case "3":
            print('value 3')
            dechiffrement()
            
        case "4":
            print('value 4')
            read_mp()
        case "5":
            print('value 5')
            encrypt_message()
        case "6":
            print('value 4')
            decrypt_message()
                                                                     
        case "Q":
            quit_program()





def quit_program():
    """Quitte le program en cours
    """
    print('Goodbye!')
    sys.exit()
    
if __name__ == '__main__':
    main_menu()                    