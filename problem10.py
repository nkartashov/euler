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

res = 0
for i in range(maxrange):
    if primes[i]:

print(sum(filter(lambda i : primes[i], range(maxrange))))
