import string
import operator

def get_cipher_text():
    
    cipher_text = input("Enter the ciphertext: ")
    return cipher_text.lower()

def letter_frequency_analysis(cipher_text, num_results=10):
    
    freq = {'a': 8.167, 'b': 1.492, 'c': 2.782, 'd': 4.253, 'e': 12.702,
            'f': 2.228, 'g': 2.015, 'h': 6.094, 'i': 6.966, 'j': 0.153,
            'k': 0.772, 'l': 4.025, 'm': 2.406, 'n': 6.749, 'o': 7.507,
            'p': 1.929, 'q': 0.095, 'r': 5.987, 's': 6.327, 't': 9.056,
            'u': 2.758, 'v': 0.978, 'w': 2.360, 'x': 0.150, 'y': 1.974,
            'z': 0.074}

    
    letter_count = {}
    for letter in string.ascii_lowercase:
        letter_count[letter] = cipher_text.count(letter)

    
    sorted_letters = sorted(letter_count.items(), key=operator.itemgetter(1), reverse=True)

    
    total_count = sum(letter_count.values())
    letter_freq = {}
    for letter, count in sorted_letters:
        letter_freq[letter] = (count / total_count) * 100

        distances = {}
    for i in range(26):
        distance = 0
        for letter in freq:
            index = (i + ord(letter) - ord('a')) % 26
            distance += abs(freq[letter] - letter_freq[chr(index + ord('a'))])
        distances[i] = distance

    
    sorted_distances = sorted(distances.items(), key=operator.itemgetter(1))

    
    print("Possible plaintexts in rough order of likelihood:")
    for i in range(num_results):
        offset = sorted_distances[i][0]
        plain_text = ""
        for letter in cipher_text:
            if letter.isalpha():
                plain_text += chr((ord(letter) - ord('a') + offset) % 26 + ord('a'))
            else:
                plain_text += letter
        print(plain_text)


def main():
    cipher_text = get_cipher_text()
    letter_frequency_analysis(cipher_text, 10)

if __name__ == '__main__':
    main()
