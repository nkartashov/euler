import math

def eratos_primes(maxrange):
    primes = [True] * maxrange

    i = 2
    while i * i < maxrange:
        if primes[i]:
            j = 2 
            while j * i < maxrange:
                primes[i * j] = False
                j += 1
        i += 1
    
    return [idx for idx, prime in enumerate(primes) if idx >= 2 and prime]

def is_prime_brut(x):
    i = 2
    while i * i <= x:
        if x % i == 0:
            return False
    return True

def is_square(x):
    sq = int(math.sqrt(x))
    return sq * sq == x
