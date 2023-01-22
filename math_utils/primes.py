from math import sqrt
def isprime(x):
    for i in range(2,int(sqrt(x)+1)):
        if x%i==0:
            return False
    return True