from collections import defaultdict

DENOMINATIONS = list(reversed([1, 2, 5, 10, 20, 50, 100, 200]))

CACHE = dict()


def get_idx(x, start):
    PRIME = 211
    return start * PRIME + x


def run_coins(x, start=0):
    if x == 0:
        return 1
    idx = get_idx(x, start)
    if idx not in CACHE:
        if start == len(DENOMINATIONS):
            return 0
        current = DENOMINATIONS[start]
        i = 0
        result = 0
        while x >= i * current:
            result += run_coins(x - i * current, start + 1)
            i += 1
        CACHE[idx] = result
    return CACHE[idx]


assert run_coins(0) == 1
assert run_coins(1) == 1
assert run_coins(2) == 2
assert run_coins(3) == 2

print(run_coins(200))
