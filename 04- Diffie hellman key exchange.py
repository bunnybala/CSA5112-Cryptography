q = 23
x = 9  
print('The prime number is : ',q)
print('The primitive root of q is : ',x)
a = 4
print('The Private Key a for Ram is : ',a) 
b = 3
print('The Private Key b for Preethi is : ',b)
s = int(pow(x,a,q))
t = int(pow(x,b,q)) 
ka = int(pow(t,a,q))
kb = int(pow(s,b,q))
print('Secret key for the Ram is : ',ka)
print('Secret Key for the Preethi is : ',kb)
