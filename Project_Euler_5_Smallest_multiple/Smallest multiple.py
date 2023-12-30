from math import gcd
for _  in range(int(input())):
    n=int(input())
    a=[i for i in range(1,n+1)]
    lcm = 1
    for i in a:
        lcm = lcm*i//gcd(lcm, i)
    print(lcm)