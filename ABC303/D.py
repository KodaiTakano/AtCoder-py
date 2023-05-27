X, Y, Z = map(int, input().split())
S = list(input())
N=len(S)
# dp[i][b]: i文字までのcapsが0,1の時の最短時間
dp=[[float("inf")]*(N+1) for _ in range(2)]
dp[0][0]=0
dp[1][0]=Z
# print(dp)
for i in range(1, N+1):
    # print(i)
    if S[i-1]=="a":
        # capsがoffにaを, capsをonからoffにしてaを押す
        dp[0][i]=min(dp[0][i-1]+X, dp[1][i-1]+Z+X)
        # capsがonの状態でShifta, capsをoffからonにしてshiftaを押す
        dp[1][i]=min(dp[1][i-1]+Y, dp[0][i-1]+Z+Y)
    else:
        # capsがonにaをたす, capsがoffの状態でShifta, capsをoffからonにしてaをたす
        dp[1][i]=min(dp[1][i-1]+X, dp[0][i-1]+Z+X)
        dp[0][i]=min(dp[0][i-1]+Y, dp[1][i-1]+Z+Y)
        
    # [print(*dp[i]) for i in range(2)]

print(min(dp[0][N], dp[1][N]))