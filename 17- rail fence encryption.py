def sequence(n):
    arr=[]
    i=0
    while(i<n-1):
        arr.append(i)
        i+=1
    while(i>0):
        arr.append(i)
        i-=1
    return(arr)
def railfence(s,n):
    s=s.lower()
    L=sequence(n)
    print("The raw sequence of indices: ",L)
    temp=L
    while(len(s)>len(L)):
        L=L+temp
    for i in range(len(L)-len(s)):
        L.pop()
    print("The row indices of the characters in the given string: ",L)
    print("Transformed message for encryption: ",s)
    num=0
    cipher_text=""
    while(num<n):
        for i in range(L.count(num)):
            cipher_text=cipher_text+s[L.index(num)]
            L[L.index(num)]=n
        num+=1
    print("The cipher text is: ",cipher_text)
plain_text=input("Enter the string to be encrypted: ")
n=int(input("Enter the number of rails: "))
railfence(plain_text,n)
