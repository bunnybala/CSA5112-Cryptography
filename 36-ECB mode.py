from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.backends import default_backend
import os


def encrypt(plaintext, key):
    # Create a cipher object with 3DES algorithm and ECB mode
    cipher = Cipher(algorithms.TripleDES(key), modes.ECB(), backend=default_backend())

    encryptor = cipher.encryptor()

    # Create a padder with the block size of the cipher
    padder = padding.PKCS7(algorithms.TripleDES.block_size).padder()

    # Pad the plaintext
    padded_plaintext = padder.update(plaintext) + padder.finalize()

    # Encrypt the padded plaintext
    ciphertext = encryptor.update(padded_plaintext) + encryptor.finalize()

    # Return the ciphertext
    return ciphertext


def decrypt(ciphertext, key):
    # Create a cipher object with 3DES algorithm and ECB mode
    cipher = Cipher(algorithms.TripleDES(key), modes.ECB(), backend=default_backend())

    decryptor = cipher.decryptor()

    # Decrypt the ciphertext
    decrypted_data = decryptor.update(ciphertext) + decryptor.finalize()

    # Create an unpadder with the block size of the cipher
    unpadder = padding.PKCS7(algorithms.TripleDES.block_size).unpadder()

    # Unpad the decrypted data
    plaintext = unpadder.update(decrypted_data) + unpadder.finalize()

    return plaintext


# Example usage
key = os.urandom(24)  # Generate a random 24-byte 3DES key
plaintext = b'This is a test message'

# Encryption
ciphertext = encrypt(plaintext, key)
print("Ciphertext:", ciphertext)

# Decryption
decrypted_text = decrypt(ciphertext, key)
print("Decrypted Text:", decrypted_text.decode())
