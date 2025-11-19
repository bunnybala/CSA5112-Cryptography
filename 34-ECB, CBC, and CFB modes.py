from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.backends import default_backend
import os


def encrypt_ecb(plaintext, key):
    
    cipher = Cipher(algorithms.AES(key), modes.ECB(), backend=default_backend())

    encryptor = cipher.encryptor()

    
    padder = padding.PKCS7(algorithms.AES.block_size).padder()

    
    padded_plaintext = padder.update(plaintext) + padder.finalize()

    
    ciphertext = encryptor.update(padded_plaintext) + encryptor.finalize()

    
    return ciphertext


def encrypt_cbc(plaintext, key, iv):
    
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())

    encryptor = cipher.encryptor()

    
    padder = padding.PKCS7(algorithms.AES.block_size).padder()

    
    padded_plaintext = padder.update(plaintext) + padder.finalize()

    
    ciphertext = encryptor.update(padded_plaintext) + encryptor.finalize()

    
    return ciphertext


def encrypt_cfb(plaintext, key, iv):
    
    cipher = Cipher(algorithms.AES(key), modes.CFB(iv), backend=default_backend())

    encryptor = cipher.encryptor()

    
    ciphertext = encryptor.update(plaintext) + encryptor.finalize()

    
    return ciphertext



key = os.urandom(16)  
iv = os.urandom(algorithms.AES.block_size // 8)  
plaintext = b'This is a test message'


ciphertext_ecb = encrypt_ecb(plaintext, key)
print("ECB Ciphertext:", ciphertext_ecb)


ciphertext_cbc = encrypt_cbc(plaintext, key, iv)
print("CBC Ciphertext:", ciphertext_cbc)


ciphertext_cfb = encrypt_cfb(plaintext, key, iv)
print("CFB Ciphertext:", ciphertext_cfb)
