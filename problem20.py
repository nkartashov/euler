f = [0 for i in range(101)]
f[0] = 1
def fac(n):
    if f[n] > 0:
        return f[n]
    f[n] = n * fac(n - 1)
    return f[n]

def s(n):
    res = 0
    for ch in str(n):
        res += int(ch)
    return res

print(s(fac(100)))

