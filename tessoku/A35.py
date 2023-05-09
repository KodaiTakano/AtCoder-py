N = int(input())
A = list(map(int, input().split()))

# dp[i][j]:上からi段目右からj個目の最適スコア
# 初期値 iが偶数の時100001、iが奇数の時-1
dp=[[-1]*N for _ in range(N)]
for i in range(N):
    if i%2!=0:
        for j in range(N):
            dp[i][j]=100001
for j in range(N):
    dp[N-1][j]=A[j]

# print(*dp)

for i in range(N-2, -1, -1):
    for j in range(i+1):
        # 太郎くんの手番(最大値)
        if i%2==0:
            dp[i][j]=max(dp[i][j], dp[i+1][j], dp[i+1][j+1])
        # 次郎くんの手番(最小値)
        else:
            dp[i][j]=min(dp[i][j], dp[i+1][j], dp[i+1][j+1])

# [print(*dp[i]) for i in range(N)]
print(dp[0][0])