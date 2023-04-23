# Using generate_key()
from cryptography.fernet import Fernet

def chiffrement(message):
    """
    Créer une fonction qui chiffrera un message.

    Args:
        message (str): Le message a dechiffrer.  

    Returns:
        str: Le mot de passe encodé.
    """
    key = Fernet.generate_key()
    f = Fernet(key)

    message_encrypt = f.encrypt(message.encode())
    
    data = {"message_encrypt":message_encrypt.decode(), "key":key.decode()}
    return data

data = chiffrement("qsdfqsdf")

print(" ========================================================== \n ")
print("Voici le mot de passe (encodé) : [ ", data["message_encrypt"], " ] ")
print("voici la cle à utiliser pour décoder le message, garder la en sécurité : [ ", data["key"], "]")
print(" \n ========================================================== ")
