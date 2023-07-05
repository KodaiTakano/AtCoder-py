from queue import Queue

# 入力
N, M = map(int, input().split())
G = [[] for _ in range(N)]
for i in range(M):
    A, B = map(int, input().split())

    # 頂点 A から頂点 B への辺を張る
    G[A-1].append(B-1)
    G[B-1].append(A-1)

ans=0
for i in range(len(G)):
    if len(G[ans])<len(G[i]):
        ans=i
print(ans+1)