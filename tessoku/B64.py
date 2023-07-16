import heapq

# 入力
N, M = map(int, input().split())
G = [[] for _ in range(N)]
for i in range(M):
    A, B, C = map(int, input().split())

    # 頂点 A から頂点 B への辺を張る
    G[A-1].append((B-1, C))
    G[B-1].append((A-1, C))

# 初期化
visited = [False] * N
dist = [float("inf")] * N

#　頂点0を始点とする
dist[0] = 0
# 最小の距離を取り出したいため、[(dist, v)]の形
pq = [(0, 0)]

# ダイクストラ法
while pq:
    # 未処理の中で最小の距離を持つ頂点を取り出す
    d, u = heapq.heappop(pq)
    # 確定済みの場合
    if visited[u]==True:
        continue

    # 訪問済みにする
    visited[u] = True

    # uから到達可能な頂点の距離を更新する
    for next_v, weight in G[u]:
        # 現在の距離
        new_dist = dist[u] + weight
        # 現在の距離の方が小さいとき
        if new_dist < dist[next_v]:
            dist[next_v] = new_dist
            heapq.heappush(pq, (new_dist, next_v))
    
# 経路復元
path=[]
place=N-1
while 1:
    path.append(place+1)
    if place == 0:
        break

    for next_v, weight in G[place]:
        # 今の距離から前の重さを引いたときに前の距離と同じのとき
        if dist[place] - weight == dist[next_v]:
            place=next_v
            break

# for d in dist:
#     if d==float("inf"):
#         print(-1)
#     else:
#         print(d)

print(*reversed(path))