import string
main=string.ascii_lowercase
def conversion(cipher_text,key):
    index=0
    plain_text=""
    cipher_text=cipher_text.lower()
    key=key.lower()
    for c in cipher_text:
        if c in main:
            off=ord(key[index])-ord('a')
            positive_off=26-off
            decrypt=chr((ord(c)-ord('a')+positive_off)%26+ord('a'))
            plain_text+=decrypt
            index=(index+1)%len(key)
        else:
            plain_text+=c
    print("cipher text: ",cipher_text)
    print("plain text (message): ",plain_text)
cipher_text=input("Enter the message to be decrypted: ")
key=input("Enter the key for decryption: ")
conversion(cipher_text,key)
