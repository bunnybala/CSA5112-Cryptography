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


bob_leaked_private_key = bob_private_key


bob_new_public_key, bob_new_private_key = generate_key_pair(p, q)


message = "Hello, world!"


ciphertext = ""
for char in message:
    m = ord(char)
    c = pow(m, bob_public_key[0], bob_public_key[1])
    ciphertext += str(c) + " "


plaintext = ""
for c in ciphertext.split():
    c = int(c)
    m = pow(c, bob_leaked_private_key[0], bob_public_key[1])
    plaintext += chr(m)

print("Bob's leaked message:", plaintext)


plaintext = ""
for c in ciphertext.split():
    c = int(c)
    m = pow(c, bob_new_private_key[0], bob_new_public_key[1])
    plaintext += chr(m)

print("Bob's new message:", plaintext)
