from sys import exit
import sys
sys.setrecursionlimit(100000)

def dfs(G, v):
    seen[v]=True
    
    if v==N-1:
        print(*path)
        exit()
    for next_v in G[v]:
        if seen[next_v]:
            continue
        path.append(next_v+1)
        dfs(G, next_v)
        path.pop()

# 入力
N, M = map(int, input().split())
G = [[] for _ in range(N)]
for i in range(M):
    A, B = map(int, input().split())

    # 頂点 A から頂点 B への辺を張る
    G[A-1].append(B-1)
    G[B-1].append(A-1)

# 各頂点が探索されたか
# False は「まだ探索されていない」ことを表す
seen = [False] * N
path=[1]
dfs(G, 0)
