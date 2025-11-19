def decrypt():
    encrypted_message = input("Enter the message i.e to be decrypted: ").strip()
    letters="abcdefghijklmnopqrstuvwxyz"
    k = int(input("Enter the key to decrypt: "))
    decrypted_message = ""
    for ch in encrypted_message:
        if ch in letters:
            position = letters.find(ch)
            new_pos = (position - k) % 26
            new_char = letters[new_pos]
            decrypted_message += new_char
        else:
            decrypted_message += ch
    print("Your decrypted message is:\n")
    print(decrypted_message)
decrypt()
