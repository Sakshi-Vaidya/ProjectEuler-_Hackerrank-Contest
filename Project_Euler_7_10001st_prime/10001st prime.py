primes = [2]
very_high_number = 1_000_000_000

def is_prime(n):
    for i in range(0, len(primes)):
        if n % primes[i] == 0:
            return False
    return True

def solve(n):
    if len(primes) >= n:
        return primes[n-1]
    
    for i in range(max(primes)+1, very_high_number):
        if (is_prime(i)):
            primes.append(i)
            if len(primes) == n:
                return primes[-1]

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    print(solve(n))