N = int(input())
A = [list(map(int, input().split())) for _ in range(N)]

B = sorted(A, reverse=False, key=lambda x: (x[1],x[0]))

# dp[i][j]:i問目まで解答するかどうか決めた時点の現在時刻がjである時、すでに最大何問解答できるか
dp=[[0]*(1441) for _ in range(N)]

for j in range(1441):
    if 0<=j-B[0][0] and j<=B[0][1]:
        dp[0][j]=1

# for i in range(10):
#     print(*dp[0][i*10:(i+1)*10])

# 何問目か
for i in range(1, N):
    # 現在時刻
    for j in range(1441):
        # i問目を解くとき
        if 0<=j-B[i][0] and j<=B[i][1]:
            dp[i][j]=max(dp[i-1][j], dp[i-1][j-B[i][0]]+1)
        else:
            dp[i][j]=dp[i-1][j]

for i in range(N):
    for j in range(2):
        print(*dp[i][j*50:(j+1)*50])
ans=0
for i in range(1441):
    ans=max(ans, dp[N-1][i])
print(ans)