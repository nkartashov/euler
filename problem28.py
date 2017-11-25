def generate_diagonal_elements(start, end):
    if end - start == 1:
        return [start]
    step = (end - start) // 4
    return list(range(start + step - 1, end, step))

assert(generate_diagonal_elements(1, 2) == [1])
assert(generate_diagonal_elements(2, 10) == [3, 5, 7, 9])
assert(generate_diagonal_elements(10, 26) == [13, 17, 21, 25])

def sum_diagonal_elements(n):
    start = 2
    length = 8
    result = 1
    while start < n * n:
        result += sum(generate_diagonal_elements(start, start + length))
        start += length 
        length += 8
    return result

assert(sum_diagonal_elements(5) == 101)

def solve():
    print(sum_diagonal_elements(1001))

solve()
