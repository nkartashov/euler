from math import log10

f1, f2 = 0,  1
i = 0
limit = 10 ** 999
while True:
    i += 1
    f1, f2 = f2, f1 + f2
    if f1 >= limit:
	print(i)
	break
