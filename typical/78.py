from queue import Queue

# 入力
N, M = map(int, input().split())
G = [[] for i in range(N)]
for i in range(M):
    A, B = map(int, input().split())

    # 頂点 A から頂点 B への辺を張る
    G[A-1].append(B-1)
    G[B-1].append(A-1)

# 各頂点が何手目に探索されたか
# -1 は「まだ探索されていない」ことを表す
dist = [-1] * N
count = [0] * N
 
# todo リストを表すキュー
que = Queue()

# 頂点 0 を始点とする
dist[0] = 0
que.put(0)

# キューが空になるまで探索する
while not que.empty():
    # キューから頂点を取り出す
    v = que.get()

    # 頂点 v から 1 手で行ける頂点 next_v を探索
    for next_v in G[v]:
        if v > next_v:
            count[v]+=1
        # 頂点 next_v が探索済みであれば何もしない
        if dist[next_v] != -1:
            continue

        # 頂点 next_v を探索する
        dist[next_v] = dist[v] + 1
        que.put(next_v)

print(count.count(1))