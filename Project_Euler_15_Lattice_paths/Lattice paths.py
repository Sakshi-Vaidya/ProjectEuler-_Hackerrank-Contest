from math import factorial
for _ in range(int(input())):
    item=input().split()
    n=int(item[0])
    m=int(item[1])
    answer=factorial(n+m)//factorial(n)//factorial(m)
    print(answer%(10**9+7))