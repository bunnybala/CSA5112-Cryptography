import math
p = int(input("Enter p: "))
q = int(input("Enter q: "))
n = p*q
print("n: ", n)
phi = (p-1)*(q-1)
print("phi: ",phi)
e = int(input("Enter e: "))
while(e<phi):
    if (math.gcd(e,phi)==1):
        break
    else:
        e+=1
print("e: ", e)
j = 0
while True:
    if ((j * e) % phi == 1):
        d = j
        break
    j += 1
print("d: ", d)
print(f'Public key: {e, n}')
print(f'Private key: {d, n}')
msg = int(input("Enter message: "))
print(f'Original message:{msg}')
C = pow(msg, e)
C = math.fmod(C, n)
print(f'Encrypted message: {C}')
M = pow(C, d)
M = math.fmod(M, n)
