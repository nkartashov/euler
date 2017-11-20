import math

import tqdm

def sqrt_ceil(x):
    return int(math.sqrt(x)) + 1

def calculate_sum_of_proper_divisors(x):
    sum = 0
    for i in range(1, sqrt_ceil(x)):
        if x % i == 0:
            sum += i
            if i != x / i and x / i != x:
                sum += x / i
    return sum

assert(calculate_sum_of_proper_divisors(12) == 16)
assert(calculate_sum_of_proper_divisors(16) == 15)

def is_abundant(x):
    return calculate_sum_of_proper_divisors(x) > x

assert(is_abundant(12))

def generate_abundant_numbers():
    low = 12
    high = 28124 - 12 # all numbers larger than 28123 can be expressed as a sum of two abundant and 12 is the smallest abundant
    return set(filter(is_abundant, range(low, high)))

def solve():
    abundant = generate_abundant_numbers()
    low = 1
    high = 28124 # see comment above
    result = 0
    for i in tqdm.tqdm(range(low, high)):
        can_be_written_as_sum = False
        for x in abundant:
            if i < x:
                break
            if i - x in abundant:
                can_be_written_as_sum = True
                break
        if not can_be_written_as_sum:
            result += i
    print(result)

solve()
