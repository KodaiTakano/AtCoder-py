S = list(input())
T = list(input())

S=["A"]+S
T=["A"]+T


dp=[[10000]*(len(T)) for _ in range(len(S))]
dp[0][0]=0
for i in range(1, len(S)):
    dp[i][0]=dp[i-1][0]+1
for j in range(1, len(T)):
    dp[0][j]=dp[0][j-1]+1

for i in range(1, len(S)):
    for j in range(1, len(T)):
        if S[i]==T[j]:
            dp[i][j]=min(dp[i-1][j]+1, dp[i][j-1]+1, dp[i-1][j-1])
        else:
            dp[i][j]=min(dp[i-1][j]+1, dp[i][j-1]+1, dp[i-1][j-1]+1)

# [print(*dp[i]) for i in range(len(S))]

print(dp[len(S)-1][len(T)-1])