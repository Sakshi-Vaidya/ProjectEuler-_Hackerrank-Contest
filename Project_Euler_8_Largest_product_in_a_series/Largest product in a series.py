def mul(s):
    prd = 1
    for i in range(len(s)):
        prd *= s[i]
    return prd    

for _ in range(int(input())):
    n,k =map(int, input().split())
    x = list(map(int, input()))
    mid = 0
    for i in range((n-k)+1):
        s = x[i : i+k]
        z = mul(s)
        if z > mid:
            mid = z                       
    print(mid)