N, W = map(int, input().split())

w=[]
v=[]
for _ in range(N):
    a, b = map(int, input().split())
    w.append(a)
    v.append(b)
INF=float("INF")
# dp[i][j] i以下の宝箱を選んでコストjの時の最小の重さ
dp=[[INF]*100001 for _ in range(N+1)]
dp[0][0]=0
for i in range(1, N+1):
    for j in range(100001):
        # iを選ばなかったときdp[i][j]=dp[i-1][j]
        # iを選んだ時dp[i][j]=min(dp[i-1][j-v[i-1]]+w[i-1], dp[i-1][j])
        if j-v[i-1]<0:
            dp[i][j]=dp[i-1][j]
        else:
            dp[i][j]=min(dp[i-1][j-v[i-1]]+w[i-1], dp[i-1][j])

ans=0
for i in range(100001):
    if dp[N][i]<=W:
        ans=i
print(ans)