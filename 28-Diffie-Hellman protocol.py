from random import randint

def diffie_hellman():
    
    q = 997

    
    a = 10

    
    x_a = randint(2, q-2)
    A = pow(a, x_a, q)

    
    x_b = randint(2, q-2)
    B = pow(a, x_b, q)

    
    shared_secret_A = pow(B, x_a, q)
    shared_secret_B = pow(A, x_b, q)

   
    assert shared_secret_A == shared_secret_B

    return shared_secret_A

print("Shared secret: ", diffie_hellman())
