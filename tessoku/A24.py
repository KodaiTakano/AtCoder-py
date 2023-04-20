import bisect
from sys import exit

N = int(input())
A = list(map(int, input().split()))

# dp[i]: 最後の要素がA[i]である部分列のうち最長のものの長さ
# L[x]: 長さxの部分文字列の最後の要素として考えられる最小値
#       dp[k]=xを満たすようなkにおけるAiの最小値

dp=[0]*(N+1)
L=[1000000]*(N+1)
L[0]=0

dp[1]=1
L[1]=A[0]
ans=1
for i in range(2, N+1):
    pos=bisect.bisect_left(L, A[i-1])
    dp[i]=pos
    
    L[dp[i]]=A[i-1]
    if dp[i]>ans:
        ans=dp[i]
    # print(i)
    # print(dp[:N+1])
    # print(L[:N+1])

print(ans)