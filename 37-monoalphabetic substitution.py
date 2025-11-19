import string
import collections


def calculate_frequency(text):
    
    frequency = collections.Counter(text)

    
    total = sum(frequency.values())
    relative_frequency = {letter: count / total for letter, count in frequency.items()}

    return relative_frequency


def decrypt(ciphertext, key):
    
    decryption_key = str.maketrans(key, string.ascii_uppercase)

    
    plaintext = ciphertext.translate(decryption_key)

    return plaintext


def perform_frequency_attack(ciphertext, num_solutions=10):
    
    ciphertext_frequency = calculate_frequency(ciphertext)

    
    sorted_frequency = sorted(ciphertext_frequency.items(), key=lambda x: x[1], reverse=True)

    
    potential_plaintexts = []

    for i in range(num_solutions):
        
        ciphertext_letter = sorted_frequency[i][0]

        
        key = ciphertext_letter * len(string.ascii_uppercase)

        
        plaintext = decrypt(ciphertext, key)

        
        potential_plaintexts.append(plaintext)

    return potential_plaintexts



ciphertext = "WKH HDVLHVW PHWKRG RI HQFLSKHULQJ D WHAW PHVVDJH LV WR UHSODFH HDFK FKDUDFWHU EB DQRWKHU XVLQJ D ILAHG UXOH, VR IRU HADPSOH HYHUB OHWWHU D PDB EH UHSODFHG EB WKH OHWWHU DQG HYHUB OHWWHU E EB WKH PDB."

potential_plaintexts = perform_frequency_attack(ciphertext, num_solutions=10)

print("Top 10 possible plaintexts:")
for i, plaintext in enumerate(potential_plaintexts):
    print(f"{i + 1}. {plaintext}")
