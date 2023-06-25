N, M = map(int, input().split())

MOD = 998244353
import math

# dp[i][b]: i人まで見て0と同じ(0)か違うか(1)どうかの時の総数
dp=[[0]*2 for _ in range(N)]
dp[0][0]=M
# print(dp)

for i in range(1, N):
    dp[i][0]+=dp[i-1][1]
    dp[i][1]+=dp[i-1][0]*(M-1)
    dp[i][1]+=dp[i-1][1]*(M-2)
    dp[i][0]%=MOD
    dp[i][1]%=MOD
print(dp[N-1][1])
    

