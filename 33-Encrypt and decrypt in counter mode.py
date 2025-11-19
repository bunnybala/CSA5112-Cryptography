S_BOX = [
    [1, 0, 3, 2],
    [3, 2, 1, 0],
    [0, 2, 1, 3],
    [3, 1, 3, 2]
]

# S-DES P4 permutation
P4 = [2, 4, 3, 1]


def generate_keys(key):
    
    key_8bit = [key[2], key[4], key[1], key[6], key[3], key[9], key[0], key[8]]

    
    p10 = [key_8bit[2], key_8bit[4], key_8bit[1], key_8bit[6], key_8bit[3], key_8bit[9], key_8bit[0], key_8bit[8], key_8bit[7], key_8bit[5]]

    
    ls1 = [p10[1], p10[2], p10[3], p10[4], p10[0], p10[6], p10[7], p10[8], p10[9], p10[5]]
    ls2 = [ls1[2], ls1[3], ls1[4], ls1[0], ls1[1], ls1[7], ls1[8], ls1[9], ls1[5], ls1[6]]

    
    key1 = [ls2[5], ls2[2], ls2[6], ls2[3], ls2[7], ls2[4], ls2[9], ls2[8]]

    
    key2 = [ls2[2], ls2[3], ls2[4], ls2[5], ls2[9], ls2[6], ls2[8], ls2[7]]

    return key1, key2


IP = [2, 6, 3, 1, 4, 8, 5, 7]


IP_INV = [4, 1, 3, 5, 7, 2, 8, 6]


EP = [4, 1, 2, 3, 2, 3, 4, 1]


P4 = [2, 4, 3, 1]


S_BOX = [
    [1, 0, 3, 2],
    [3, 2, 1, 0],
    [0, 2, 1, 3],
    [3, 1, 3, 2]
]


def f_function(key, plaintext):
    
    expanded_plaintext = [plaintext[EP[i] - 1] for i in range(8)]

    
    xored_plaintext = [expanded_plaintext[i] ^ key[i] for i in range(8)]
