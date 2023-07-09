N, M = map(int, input().split())
p = list(map(int, input().split()))
A = [list(map(int, input().split())) for _ in range(M)]

from collections import defaultdict

# 親iが最大何世代先まで保険に入れたか
d=defaultdict(int)
for i in range(M):
    d[A[i][0]-1] = max(d[A[i][0]-1], A[i][1])
# print(d)

from collections import deque

# 入力
G = [[] for _ in range(N)]
for i in range(N-1):
    # 頂点 A から頂点 B への辺を張る
    G[p[i]-1].append(i+1)
# print(G)

# 各頂点が何手目に探索されたか
# -1 は「まだ探索されていない」ことを表す
dist = [0] * N
for k, v in d.items():
    dist[k]=v+1
# print(dist)

# todo リストを表すキュー
que = deque()

que.append(0)

# キューが空になるまで探索する
while que:
    # キューから頂点を取り出す
    v = que.popleft()

    # 頂点 v から 1 手で行ける頂点 next_v を探索
    for next_v in G[v]:
        # 頂点 next_v を探索する
        dist[next_v] = max(dist[next_v], dist[v]-1)
        que.append(next_v)

# print(dist)
ans=0
for i in range(N):
    if dist[i]!=0:
        ans+=1

print(ans)