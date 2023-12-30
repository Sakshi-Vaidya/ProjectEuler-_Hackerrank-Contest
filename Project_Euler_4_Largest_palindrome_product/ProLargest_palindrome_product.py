import sys

def r_num(n):
    l_pal=0
    for i in range(999,100,-1):
        for j in range(999,100,-1):
            m = i*j
            if (m>=101101 and m<n):
                if str(m)== str(m)[::-1]:
                    l_pal = max(m,l_pal)
                    break
    return l_pal

            
t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    print(r_num(n))

    