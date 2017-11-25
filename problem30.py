import tqdm

POWERS = list(map(lambda x : x ** 5, range(0, 10)))

def solve():
    result = 0
    for i in tqdm.tqdm(range(POWERS[-1] * 5)):
        s = str(i)
        if len(s) == 1:
            continue
        value = sum(POWERS[int(e)] for e in s)
        if value == i:
            result += i
    print(result)

solve()
