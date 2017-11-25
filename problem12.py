maxrange = 2000001
primes = [True] * maxrange

i = 2
while i * i < maxrange:
    if primes[i]:
        j = 2 
        while j * i < maxrange:
            primes[i * j] = False
            j += 1
    i += 1


p = map(lambda x : x[0], filter(lambda e : e[1], enumerate(primes)))[2:]

def divisors(n):
    d = []
    i = 0
    while p[i] <= n:
        counter = 0
        while n % p[i] == 0:
            n /= p[i]
            counter += 1
        d.append(counter + 1)
        i += 1
    
    return reduce(lambda x, y : x * y, d)

k = 10
while True:
    res = 0
    if k % 2 == 0:
        res = divisors(k / 2) * divisors(k + 1)
    else:
        res = divisors(k) * divisors((k + 1) / 2) 
    if res >= 500:
        print((k + 1) * k / 2)
        break
    k += 1
