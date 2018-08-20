import math

def sieve(num):
    
    primes = [True] * (num + 1)
    primes[0] = False 
    primes[1] = False
    for i in range(math.floor(math.sqrt(num))):
        if primes[i]:
            for j in range(i*2, j <= num, i):
                primes[j] = False
    print(primes)
sieve(100)