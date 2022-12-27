N, S = map(int, input().split())
A = list(map(int, input().split()))

# dp[i][j]:iまでのカードを選んで合計がjがありえるか
dp = [[0]*(S+1) for _ in range(N+1)]
dp[0][0]=1
for i in range(1, N+1):
    for j in range(S+1):
        if dp[i-1][j]==1:
            dp[i][j]=1
        if dp[i-1][j]==1 and j+A[i-1]<=S:
            dp[i][j+A[i-1]]=1
if dp[N][S]==1:
    print("Yes")
else:
    print("No")
# [print(dp[i]) for i in range(N+1)]