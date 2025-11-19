import random

initial_key = random.getrandbits(64)


def split_key(key):
    left = key >> 28
    right = key & 0xFFFFFFF
    return left, right


def combine_key(left, right):
    return (left << 28) | right


def shift_key_left(key, n):
    return ((key << n) & 0xFFFFFFF) | (key >> (28 - n))


shifts = [1, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1]
subkeys = []
key = initial_key
for i in range(16):
    left, right = split_key(key)
    left = shift_key_left(left, shifts[i])
    right = shift_key_left(right, shifts[i])
    subkey = combine_key(left, right)
    subkeys.append(subkey)
    key = subkey
print("Subkeys:")
for i, subkey in enumerate(subkeys):
    print(f"{i + 1}:{subkey:016X}")
