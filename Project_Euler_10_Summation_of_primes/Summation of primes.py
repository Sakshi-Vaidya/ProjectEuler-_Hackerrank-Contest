import math

limit=10**6
sieve=[True]*(limit+1)
sieve[0]=sieve[1]=False

for idx in range(2,int(math.sqrt(limit)+1)):
    if sieve[idx]:
        for multiple in range(idx*idx,limit+1,idx):
            sieve[multiple]=False

cumultative_sum = [0]
current_sum=0
for i in range(1,limit+1):
    if sieve[i]:
        current_sum+=i
    cumultative_sum.append(current_sum)


t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    print(cumultative_sum[n])