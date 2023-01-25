import math

import tqdm

from common import eratos_primes, is_square

TWO_MIL = 42_000_000

PRIMES = eratos_primes(TWO_MIL)
PRIMES_SET = set(PRIMES)


def is_palindrome(s: str) -> int:
    i = 0
    j = len(s) - 1
    while i < j:
        if s[i] != s[j]:
            return False
        i += 1
        j -= 1

    return True


def is_reversible_prime_square(x: int) -> bool:
    reverse = int("".join(reversed(str(x))))

    assert math.sqrt(reverse) < TWO_MIL

    return (
        not is_palindrome(str(x))
        and is_square(reverse)
        and int(math.sqrt(reverse)) in PRIMES_SET
    )


assert is_reversible_prime_square(169)


def solve():
    count = 0
    result = 0
    for x in tqdm.tqdm(PRIMES):
        if is_reversible_prime_square(x * x):
            result += x * x
            count += 1
            if count == 50:
                break

    return result


print(solve())
