from collections import deque
import heapq

N, T = map(int, input().split())
G = [[] for _ in range(N)]

for i in range(N-1):
    A, B = map(int, input().split())
    G[A-1].append(B-1)
    G[B-1].append(A-1)

# 各頂点が何手目に探索されたか
# -1 は「まだ探索されていない」ことを表す
dist = [-1] * N

# todo リストを表すキュー
que = deque()

# 頂点 0 を始点とする
dist[T-1] = 0
que.append(T-1)

# キューが空になるまで探索する
while que:
    # キューから頂点を取り出す
    v = que.popleft()

    # 頂点 v から 1 手で行ける頂点 next_v を探索
    for next_v in G[v]:
        # 頂点 next_v が探索済みであれば何もしない
        if dist[next_v] != -1:
            continue

        # 頂点 next_v を探索する
        dist[next_v] = dist[v] + 1
        que.append(next_v)

# print(dist)

# [(-dist, index)]
pq = []

for i in range(N):
    heapq.heappush(pq, (-dist[i], i))
# print(pq)
# d, index= heapq.heappop(pq)
# print(d, index)

visited=[False]*N
ans=[0]*N

while pq:
    d, u = heapq.heappop(pq)
    # print(d, u)
    for next_v in G[u]:
        if dist[u] > dist[next_v]:
            ans[next_v]=max(ans[next_v], ans[u]+1)
print(*ans)