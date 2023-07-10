from sys import exit
import sys
sys.setrecursionlimit(100000)

def dfs(G, v):
    seen[v]=True
    for next_v in G[v]:
        if seen[next_v]:
            continue
        dfs(G, next_v)

# 入力
N, M = map(int, input().split())
G = [[] for _ in range(N)]
for i in range(M):
    A, B = map(int, input().split())

    # 頂点 A から頂点 B への辺を張る
    G[A-1].append(B-1)
    G[B-1].append(A-1)

seen = [False] * N
dfs(G, 0)

for b in seen:
    if not b:
        print("The graph is not connected.")
        exit()
print(" The graph is connected.")