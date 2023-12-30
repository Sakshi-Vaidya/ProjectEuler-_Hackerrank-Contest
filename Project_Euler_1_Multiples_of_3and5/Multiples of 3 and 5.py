t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    answer=0
    k=(n-1)//3
    answer+=3*k*(k+1)//2
    k=(n-1)//5
    answer+=5*k*(k+1)//2
    k=(n-1)//15
    answer-=15*k*(k+1)//2
    print(answer)
