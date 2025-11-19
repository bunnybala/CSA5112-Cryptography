P10 = [3, 5, 2, 7, 4, 10, 1, 9, 8, 6]
P8 = [6, 3, 7, 4, 8, 5, 10, 9]
EP = [4, 1, 2, 3, 2, 3, 4, 1]
P4 = [2, 4, 3, 1]
IP = [2, 6, 3, 1, 4, 8, 5, 7]
IP_INV = [4, 1, 3, 5, 7, 2, 8, 6]
S0 = [[1, 0, 3, 2], [3, 2, 1, 0], [0, 2, 1, 3], [3, 1, 3, 2]]
S1 = [[0, 1, 2, 3], [2, 0, 1, 3], [3, 0, 1, 0], [2, 1, 0, 3]]


def apply_permutation(bits, permutation):
    return ''.join(bits[i - 1] for i in permutation)


def generate_round_keys(key):
    round_keys = []
    key = apply_permutation(key, P10)
    left, right = key[:5], key[5:]
    for i in range(2):
        left = left[1:] + left[0]
        right = right[1:] + right[0]
        round_key = apply_permutation(left + right, P8)
        round_keys.append(round_key)
    return round_keys


def f_function(bits, round_key):
    expanded = apply_permutation(bits, EP)
    xored = bin(int(expanded, 2) ^ int(round_key, 2))[2:].zfill(8)
    left, right = xored[:4], xored[4:]
    sbox_output = apply_sbox(left, S0) + apply_sbox(right, S1)
    return apply_permutation(sbox_output, P4)


def apply_sbox(bits, sbox):
    row = int(bits[0] + bits[3], 2)
    col = int(bits[1:3], 2)
    return format(sbox[row][col], '02b')


def encrypt_block(block, round_keys):
    block = apply_permutation(block, IP)
    left, right = block[:4], block[4:]
    for i in range(2):
        f_result = f_function(right, round_keys[i])
        new_right = bin(int(left, 2) ^ int(f_result, 2))[2:].zfill(4)
        left = right
        right = new_right
    cipher_text = apply_permutation(right + left, IP_INV)
    return cipher_text


def decrypt_block(block, round_keys):
    block = apply_permutation(block, IP)
    left, right = block[:4], block[4:]
    for i in range(2):
        f_result = f_function(right, round_keys[1 - i])
        new_right = bin(int(left, 2) ^ int(f_result, 2))[2:].zfill(4)
        left = right
        right = new_right
    plain_text = apply_permutation(right + left, IP_INV)
    return plain_text



def cbc_encrypt(plaintext, key, iv):
    ciphertext = []
    round_keys = generate_round_keys(key)
    previous_cipher_block = iv
    for block in plaintext:
        block = bin(int(block, 2) ^ int(previous_cipher_block, 2))[2:].zfill(8)
        encrypted_block = encrypt_block(block, round_keys)
        ciphertext.append(encrypted_block)
        previous_cipher_block = encrypted_block
    return ciphertext



def cbc_decrypt(ciphertext, key, iv):
    plaintext = []
    round_keys = generate_round_keys(key)
    previous_cipher_block = iv
    for block in ciphertext:
        decrypted_block = decrypt_block(block, round_keys)
        decrypted_block = bin(int(decrypted_block, 2) ^ int(previous_cipher_block, 2))[2:].zfill(8)
        plaintext.append(decrypted_block)
        previous_cipher_block = block
    return plaintext



plaintext = ['00000001', '00100011']
key = '0111111101'
iv = '10101010'


ciphertext = cbc_encrypt(plaintext, key, iv)
print("Ciphertext:", ciphertext)
