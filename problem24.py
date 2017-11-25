import tqdm

def next_permutation(a):
    pivot = 2
    while a[-pivot] >= a[-pivot + 1]:
        pivot += 1
    succ = 1
    while a[-succ] <= a[-pivot]:
        succ += 1
    a[-succ], a[-pivot] = a[-pivot], a[-succ]
    a[-pivot + 1:] = reversed(a[-pivot + 1:])
    return a

assert(next_permutation([0, 1, 2, 5, 3, 3, 0]) == [0, 1, 3, 0, 2, 3, 5])

START_PERM = list(range(0, 10))

def solve():
    a = START_PERM.copy()
    for i in tqdm.tqdm(range(1, 1000000)):
        next_permutation(a)

    print(''.join(map(str, a)))

solve()
