def generate_subkeys(block_size):
    if block_size == 64:
        constant = 0x1B
    elif block_size == 128:
        constant = 0x87
    else:
        raise ValueError("Invalid block size")

    zero_block = bytes([0] * (block_size // 8))

    
    ciphertext = block_cipher(zero_block)

   
    left_shifted = left_shift(ciphertext, block_size)

    
    subkey1 = xor(left_shifted, constant)

    
    subkey2 = left_shift(subkey1, block_size)

    return subkey1, subkey2


def block_cipher(block):
        return block


def left_shift(data, block_size):
   
    shifted = bytearray(data)
    shift_amount = 1
    while shift_amount < block_size:
        carry = 0
        for i in range(len(shifted) - 1, -1, -1):
            temp = shifted[i] & 0x80
            shifted[i] = ((shifted[i] << 1) & 0xFF) | carry
            carry = temp >> 7
        shift_amount += 1
    return bytes(shifted)


def xor(data, constant):
    
    xored = bytearray(data)
    for i in range(len(xored)):
        xored[i] ^= constant
    return bytes(xored)



subkey1, subkey2 = generate_subkeys(64)
print("Subkey 1 (64-bit):", subkey1.hex())
print("Subkey 2 (64-bit):", subkey2.hex())


subkey1, subkey2 = generate_subkeys(128)
print("Subkey 1 (128-bit):", subkey1.hex())
print("Subkey 2 (128-bit):", subkey2.hex())
