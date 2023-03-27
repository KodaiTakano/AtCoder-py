N = int(input())
S = list(input())

# dp[i][j]: i文字目からj文字目までの部分における最長回文
dp=[[0]*N for _ in range(N)]
for i in range(N):
    dp[i][i]=1
for i in range(N-1):
    if S[i]==S[i+1]:
        dp[i][i+1]=2
    else:
        dp[i][i+1]=1
# [print(*dp[i]) for i in range(N)]

for i in range(N-1, -1, -1):
    for j in range(N):
        if j-i<=1:
            continue
        # print(i, j)
        elif S[i]==S[j]:
            dp[i][j]=max(dp[i+1][j], dp[i][j-1], dp[i+1][j-1]+2)
        else:
            dp[i][j]=max(dp[i+1][j], dp[i][j-1])
        # dp[i][j]=9
        # [print(*dp[i]) for i in range(N)]
        
# [print(*dp[i]) for i in range(N)]
print(dp[0][N-1])