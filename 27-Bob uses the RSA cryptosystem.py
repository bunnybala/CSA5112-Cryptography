import math


def generate_key_pair(p, q):
    n = p * q
    phi = (p-1) * (q-1)
    e = 65537
    d = pow(e, -1, phi)
    return (e, n), (d, n)


p = 61
q = 53


bob_public_key, bob_private_key = generate_key_pair(p, q)


def encrypt_message(message, public_key):
    ciphertext = ""
    for char in message:
        m = ord(char) - ord('A')
        c = pow(m, public_key[0], public_key[1])
        ciphertext += str(c) + " "
    return ciphertext


def decrypt_message(ciphertext, private_key):
    plaintext = ""
    for c in ciphertext.split():
        c = int(c)
        m = pow(c, private_key[0], private_key[1])
        plaintext += chr(m + ord('A'))
    return plaintext


message = "HELLO WORLD"


ciphertext = encrypt_message(message, bob_public_key)


def frequency_analysis(ciphertext):
    frequencies = [0] * 26
    for c in ciphertext.split():
        c = int(c)
        for i in range(26):
            if pow(i, bob_public_key[0], bob_public_key[1]) == c:
                frequencies[i] += 1
    return frequencies


frequencies = frequency_analysis(ciphertext)


for i in range(26):
    print(chr(i + ord('A')), ":", frequencies[i])


plaintext = decrypt_message(ciphertext, bob_private_key)

print("Decrypted message:", plaintext)
