def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)
def is_coprime(a, b):
    return gcd(a, b) == 1
def is_valid_affine(a, b):
    return is_coprime(a, 26) and b >= 0 and b < 26
def encrypt_affine(msg, a, b):
    ciphertext = ''
    for c in msg:
        if c.isalpha():
            idx = ord(c.upper()) - ord('A')
            idx = (a * idx + b) % 26
            ciphertext += chr(idx + ord('A'))
        else:
            ciphertext += c
    return ciphertext
msg =input("Enter the plain text: ")
a = 5
b = 7
if is_valid_affine(a, b):
    ciphertext = encrypt_affine(msg, a, b)
    print("plaintext:", msg)
    print("Ciphertext:", ciphertext)
else:
    print("Invalid values of a and/or b.")
