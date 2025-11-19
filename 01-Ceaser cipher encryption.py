P="hello everyone"
lst1= []
plaintext= []
for i in range(97,123):
    lst1.append(chr(i))
print(lst1)
k=[]
for j in lst1:
    k.append(lst1.index(j))
print(k)
for i in P:
    if i in lst1:
        print(lst1.index(i))
        plaintext.append(lst1.index(i))
print(plaintext)
cipher=[x+1 for x in plaintext]
print(cipher)
for m in cipher:
    if m in k:
        print(lst1[m],end="")
