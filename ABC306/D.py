N = int(input())

# dp[i][bool]:i番目まで食べた時,お腹を壊しているかどうかでの美味しさの総和の最大値
dp=[[0]*(2) for  _ in range(N+1)]

for i in range(N):
    X, Y = map(int, input().split())
    # Xが0の時
    if X==0:
        dp[i+1][0]=max(dp[i][0], dp[i][0]+Y, dp[i][1]+Y)
        dp[i+1][1]=dp[i][1]
    else:
        dp[i+1][0]=dp[i][0]
        dp[i+1][1]=max(dp[i][1], dp[i][0]+Y)
    # [print(*dp[i]) for i in range(N+1)]
    # print()
print(max(dp[N][0], dp[N][1]))