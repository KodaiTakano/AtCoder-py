N = int(input())

P=[]
A=[]
for _ in range(N):
    p, a = map(int, input().split())
    P.append(p)
    A.append(a)

# dp[i][j]: i番目からj番目まで残っている状態での最高得点
dp=[[0]*N for _ in range(N)]
dp[0][N-1]=0

for i in range(0, N):
    for j in range(N-1, -1, -1):
        if i==0 and j==N-1:
            continue
        if i>j:
            continue
        
        # 左を取り除く
        s1=0
        if i!=0:
            if i<=P[i-1]-1 and P[i-1]-1<=j:
                s1=A[i-1]

        s2=0
        # 右を取り除く
        if j!=N-1:
            if i<=P[j+1]-1 and P[j+1]-1<=j:
                s2=A[j+1]


        if i==0:
            dp[i][j]=dp[i][j+1]+s2
        elif j==N-1:
            dp[i][j]=dp[i-1][j]+s1
        else:
            dp[i][j]=max(dp[i][j+1]+s2, dp[i-1][j]+s1)
        
        # print(i, j)
        # print(s2)
        # [print(*dp[k]) for k in range(N)]

ans=0
for i in range(N):
    ans=max(ans, dp[i][i])
print(ans)