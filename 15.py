dim = 21
paths = []
for i in range(dim):
    paths.append([0 for j in range(dim)])

paths[0][0] = 1

def in_f(i, j):
    return 0 <= i < dim and 0 <= j < dim

def p(i, j):
    if not in_f(i, j):
        return 0

    if (paths[i][j] > 0):
        return paths[i][j]

    pth = p(i - 1, j) + p(i, j - 1)
    paths[i][j] = pth
    return pth

for i in range(dim):
    for j in range(dim):
        p(i, j)

print(p(20, 20))

