import sys

N, S = map(int, input().split())
A = list(map(int, input().split()))

# dp[i][j]: i以下を選んで合計jとなりうるか
dp=[[0]*(S+1) for _ in range(N+1)]
dp[0][0]=1

for i in range(1, N+1):
    for j in range(S+1):
        if dp[i-1][j]==1:
            dp[i][j]=1
        if j-A[i-1]>=0 and dp[i-1][j-A[i-1]]==1:
            dp[i][j]=1
# [print(*dp[i]) for i in range(N+1)]

if dp[N][S]==0:
    print(-1)
    sys.exit()

i=N
j=S
ans=[]
while(True):
    # print(i, j)
    if j-A[i-1]>=0 and dp[i-1][j-A[i-1]]==1:
        ans.append(i)
        j-=A[i-1]
        i-=1
    else:
        i-=1
    if i==0:
        break
    # print(ans)
print(len(ans))
print(*reversed(ans))