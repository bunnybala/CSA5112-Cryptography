from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import padding
import os


def cbc_mac(key, message):
    iv = os.urandom(16)  

    
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    encryptor = cipher.encryptor()

    
    padder = padding.PKCS7(128).padder()
    padded_message = padder.update(message) + padder.finalize()

   
    ciphertext = encryptor.update(padded_message) + encryptor.finalize()

    return ciphertext



key = os.urandom(32)


message = b"Hello, CBC-MAC!"


mac = cbc_mac(key, message)
print("MAC for one-block message:", mac.hex())


two_block_message = message + bytes(x ^ y for x, y in zip(message, mac))


print("CBC MAC for two-block message:", cbc_mac(key, two_block_message).hex())
