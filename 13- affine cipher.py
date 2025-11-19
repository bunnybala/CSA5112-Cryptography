ct=str(input("ENTER THE PLAIN TEXT : "))
a=int(input("ENTER a : "))
b=int(input("ENTER b : "))
letter="abcdefghijklmnopqrstuvwxyz"
dec=""
for x in ct:
    en=0
    if x in letter:
        pos=letter.find(x)
        en=((a*pos)+b)%26
        dec+=letter[en]
print("CIPHER TEXT : "+dec)
