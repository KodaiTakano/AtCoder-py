from sys import exit

MOD = 998244353

S = list(input())

if len(S)==1:
    print(0)
    exit()
if S[0]==")":
    print(0)
    exit()

dp=[[0]*len(S) for _ in range(len(S))]
dp[0][1]=1

for i in range(1, len(S)):
    for j in range(len(S)):
        if S[i]=="(" and j>0:
            dp[i][j]+=dp[i-1][j-1]%MOD
        if S[i]==")" and j<len(S)-1:
            dp[i][j]+=dp[i-1][j+1]%MOD
        if S[i]=="?":
            if j>0:
                dp[i][j]+=dp[i-1][j-1]%MOD
            if j<len(S)-1:
                dp[i][j]+=dp[i-1][j+1]%MOD
# [print([*dp[i]]) for i in range(len(S))]

print(dp[len(S)-1][0]%MOD)