import sys

t = int(input())
for _ in range(t):
    n = int(input())
    fact = 1
    for x in range(1,n+1):
        fact *= x
    
    sum = 0
    while(fact>0):
        r = fact%10
        sum += r
        fact = fact//10
        
    print(sum)