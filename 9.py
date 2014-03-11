from math import sqrt

for i in range(1000):
    i2 = i * i * 1.0
    for j in range (1000):
        if i + j + sqrt(j * j + i2) == 1000:
            print(i, j)
