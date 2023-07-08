N1, N2, M = map(int, input().split())

from collections import deque

G = [[] for _ in range(N1+N2)]
for i in range(M):
    A, B = map(int, input().split())

    # 頂点 A から頂点 B への辺を張る
    G[A-1].append(B-1)
    G[B-1].append(A-1)

# 各頂点が何手目に探索されたか
# -1 は「まだ探索されていない」ことを表す
dist1 = [-1] * (N1+N2)
dist2 = [-1] * (N1+N2)

# todo リストを表すキュー
que1 = deque()
que2 = deque()

# 頂点 0 を始点とする
dist1[0] = 0
que1.append(0)
dist2[N1+N2-1] = 0
que2.append(N1+N2-1)


# キューが空になるまで探索する
while que1:
    # キューから頂点を取り出す
    v = que1.popleft()

    # 頂点 v から 1 手で行ける頂点 next_v を探索
    for next_v in G[v]:
        # 頂点 next_v が探索済みであれば何もしない
        if dist1[next_v] != -1:
            continue

        # 頂点 next_v を探索する
        dist1[next_v] = dist1[v] + 1
        que1.append(next_v)

while que2:
    # キューから頂点を取り出す
    v = que2.popleft()

    # 頂点 v から 1 手で行ける頂点 next_v を探索
    for next_v in G[v]:
        # 頂点 next_v が探索済みであれば何もしない
        if dist2[next_v] != -1:
            continue

        # 頂点 next_v を探索する
        dist2[next_v] = dist2[v] + 1
        que2.append(next_v)

print(max(dist1)+max(dist2)+1)