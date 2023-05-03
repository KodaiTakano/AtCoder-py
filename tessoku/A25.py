H, W = map(int, input().split())
B = [list(input()) for _ in range(H)]

# dp[i][j]:マスijまでに行く方法の総数
dp=[[0]*W for _ in range(H)]

dp[0][0]=1
for i in range(1, H):
    if B[i][0]=="#":
        dp[i][0]=0
    else:
        dp[i][0]=dp[i-1][0]

for j in range(1, W):
    if B[0][j]=="#":
        dp[0][j]=0
    else:
        dp[0][j]=dp[0][j-1]

for i in range(1, H):
    for j in range(1, W):
        if B[i][j]=="#":
            dp[i][j]=0
        else:
            dp[i][j]=dp[i-1][j]+dp[i][j-1]

# [print(*B[i]) for i in range(H)]
# [print(*dp[i]) for i in range(H)]

print(dp[H-1][W-1])