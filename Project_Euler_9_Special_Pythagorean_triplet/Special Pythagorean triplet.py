import math

def find_maximum_pythagorean_triplet(n):
    if n % 2 != 0:
        return -1

    m = -1
    for a in range(1, (n // 3) + 1):
        b = n * (n - 2 * a) // (2 * (n - a))
        c = n - a - b
        if a ** 2 + b ** 2 == c ** 2:
            m = max(m, a * b * c)
    return m

t = int(input())
for _ in range(t):
    n = int(input())
    print(find_maximum_pythagorean_triplet(n))