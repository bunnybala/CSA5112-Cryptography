import string
plain_text = "hello world"
key = 1
alphabet = string.ascii_lowercase
keyvalue = alphabet[key:] + alphabet[:key]
table = str.maketrans(alphabet, keyvalue)
encrypted = plain_text.translate(table)
print(encrypted)
