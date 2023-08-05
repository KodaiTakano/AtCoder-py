N = int(input())
A = list(map(int, input().split()))

ave=sum(A)/N

ave1=int(ave)
ave2=int(ave)+1

sum1=0
sum2=0
for i in range(N):
    if A[i]<=ave1:
        sum1+=ave1-A[i]
    if ave2<=A[i]:
        sum2+=A[i]-ave2
print(max(sum1, sum2))