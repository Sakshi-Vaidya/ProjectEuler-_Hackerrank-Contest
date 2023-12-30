import sys
import math
max_N=1000000

def makeEras(n):
    check_prime=[True for _ in range(n+1)]
    result=[]
    for i in range(2, n+1):
        if check_prime[i]:
            result.append(i)
            for j in range(2, n//i+1):
                check_prime[i*j]=False
    return result
prime=makeEras(max_N)
def smallest_prime_factor(n):
    for x in prime:
        if n% x==0:
            return x
    return n

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    while n>smallest_prime_factor(n):
        n=n//smallest_prime_factor(n)
    print(n)
