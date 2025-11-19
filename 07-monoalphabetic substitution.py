pt=str(input("ENTER THE PLAIN TEXT : "))
cipher=""
letter="abcdefghijklmnopqrstuvwxyz"
common=max(set(pt),key=pt.count)
print("COMMON LETTER : "+common)
if common in letter:
    com=letter.find(common)
key=com-6
#print("key = "+common+" - g = "+key)
if (key<0):
    key=26-key
for i in pt:
    if i in letter:
        pos=letter.find(i)
        new_pos=(pos+key)%26
        new_char=letter[new_pos]
        cipher+=new_char
print("CIPHER TEXT : "+cipher)
