# Using generate_key()
from cryptography.fernet import Fernet


def dechiffrement(message_encrypt, key):
    """
    Créer une fonction dechiffrement d'un message.

    Args:
        message_encrypt : Le message_encodé a décoder.  
        key : key d'encryption
        
    Returns:
        str: le mot de passe en clair.

        Il est à noter que l'on remplace les variables : 
        - message_encrypt
        - key 
        en dur dans le script
    """
    f = Fernet(key)

    message_decrypt = f.decrypt(message_encrypt.encode())
    
    data={"message_decrypt":message_decrypt.decode(),"key":key}
    return data

message_encrypt = "gAAAAABkQb-9ZCGrSNQdzh8XJ89jSE5W8meFfd7t_ak342FVhuy5h2hFaDT6Ai6OJBAIA96FTPBwl8Scy9shzQGcyzRY8gaPoA=="
key = "Vb_4ZwGhvIImlr5Ka8lo6u9i9-7iwNS0Yqm4ANge3CE="


data = dechiffrement(message_encrypt, key)

print(" ========================================================== \n ")
print("Voici le mot de passe (décodé) : ", data["message_decrypt"])

print(" \n ========================================================== ")
