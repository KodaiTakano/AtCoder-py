N, W = map(int, input().split())

w=[]
v=[]
for _ in range(N):
    a, b = map(int, input().split())
    w.append(a)
    v.append(b)

# dp[i][j]:i番目まで選んで重さjの時の最大コスト
dp=[[0]*(W+1) for _ in range(N+1)]

for i in range(1, N+1):
    for j in range(1, W+1):
        # print(i, j)
        if j-w[i-1]>=0:
            dp[i][j]=max(dp[i][j-1], dp[i-1][j], dp[i-1][j-w[i-1]]+v[i-1])
        else:
            dp[i][j]=max(dp[i][j-1], dp[i-1][j])
# [print(*dp[i]) for i in range(N+1)]
print(max(dp[N]))
