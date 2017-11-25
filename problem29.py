import tqdm

def solve():
    powers = set()
    for a in tqdm.tqdm(range(2, 101)):
        for b in range(2, 101):
            power = a ** b
            if power not in powers:
                powers.add(power)
    print(len(powers))

solve()
