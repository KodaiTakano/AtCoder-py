N = int(input())

A, B, C = map(int, input().split())

ans=10000
for i in range(10000):
    if N-A*i<0:
        break
    for j in range(10000-i):
        sum = N-A*i-B*j
        if sum>=0 and sum%C==0:
            ans = min(ans, sum/C+i+j)
print(int(ans))

