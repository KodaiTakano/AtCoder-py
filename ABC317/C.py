import sys
sys.setrecursionlimit(100000)

def dfs(G, v, d):
    global temp_ans
    seen[v]=True
    if d > temp_ans:
        temp_ans=d
    for i in range(N):
        if  not seen[i] and G[v][i]:
            dfs(G, i, d+G[v][i])
    seen[v]=False

    return temp_ans

# 入力
N, M = map(int, input().split())
G = [[0]*N for _ in range(N)]
for i in range(M):
    A, B, C = map(int, input().split())

    # 頂点 A から頂点 B への辺を張る
    G[A-1][B-1]=C
    G[B-1][A-1]=C

# 各頂点が探索されたか
# False は「まだ探索されていない」ことを表す
# ans=0
# for i in range(N):
#     temp_ans=0
#     seen = [False] * N
#     ans = max(ans, dfs(G, i, 0))

ans=0
seen=[False]*N
for i in range(N):
    temp_ans=0
    ans = max(ans, dfs(G, i, 0))
print(ans)