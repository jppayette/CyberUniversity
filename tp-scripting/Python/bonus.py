from cryptography.fernet import Fernet
import base64
import os
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC


def read_mdp(fichier):
    """
    Créer une fonction de chiffrement d'un message depuis un fichier

    Args:
        file (file): le nom du fichier contenant le passwd  

    Returns:
        str: le mot de passe encodé.
    """

    with open(fichier, "r") as f:
        premier_mot = f.readline().split()[0]
    
    password = premier_mot.encode()
    # lire le password depuis le fichier
    
    salt = os.urandom(16)
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=480000,
    )

    key = base64.urlsafe_b64encode(kdf.derive(password))
    f = Fernet(key)
    
    token_encrypt = f.encrypt(password)
    print(token_encrypt)

    print('key', key)

    token_decrypt = f.decrypt(token_encrypt)
    print(token_decrypt)

read_mdp('toto.txt')