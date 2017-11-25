def find_repeating_length(divisor):
    remainder = 1
    current_division = 0
    known_remainders = dict()
    while True:
        if remainder == 0:
            return 0
        current_division += 1
        while remainder < divisor:
            remainder *= 10
        if remainder in known_remainders:
            return current_division - known_remainders[remainder]
        known_remainders[remainder] = current_division
        remainder = remainder % divisor

assert(find_repeating_length(3) == 1)
assert(find_repeating_length(6) == 1)
assert(find_repeating_length(7) == 6)
assert(find_repeating_length(9) == 1)

def solve():
    result = 3
    cycle = 1
    for i in range(2, 1000):
        new_cycle = find_repeating_length(i)
        if new_cycle > cycle:
            result = i
            cycle = new_cycle
    print(result)

solve()
