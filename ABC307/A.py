N = int(input())
A = list(map(int, input().split()))

ans=0
for i in range(7*N):
    ans+=A[i]
    if i!=0 and (i+1)%7==0:
        print(ans, end=" ")
        ans=0