# 入力
N = int(input())
G = [[] for _ in range(N)]
A = list(map(int, input().split()))
for i in range(N-1):
    # 部下から上司への辺を張る
    G[A[i]-1].append(i+1)
    
# [print(*G[i]) for i in range(N)]

# dp[i]:iの社員は何人部下がいるか
dp = [0] * N

# 上司i
for i in range(N-1, -1, -1):
    dp[i]=len(G[i])
    for j in range(len(G[i])):
        # 上司iの部下の数+それぞれの部下の部下の数
        dp[i] += dp[G[i][j]]
print(*dp)