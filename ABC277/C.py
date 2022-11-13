from itertools import chain
import sys

N = int(input())

AB=[]
for _ in range(N):
    a, b = map(int, input().split())
    AB.append([a, b])
flattenAB=sorted(set(list(chain.from_iterable(AB))))
if flattenAB[0]!=1:
    print(1)
    sys.exit()

dictAB={v:i for i, v in enumerate(flattenAB)}
for i in range(N):
    AB[i][0]=dictAB[AB[i][0]]
    AB[i][1]=dictAB[AB[i][1]]

# print(AB)

from queue import Queue

# 入力
M=N
N=len(dictAB)
G = [[] for i in range(N)]
for i in range(M):

    # 頂点 A から頂点 B への辺を張る
    G[AB[i][0]].append(AB[i][1])
    G[AB[i][1]].append(AB[i][0])

# 各頂点が何手目に探索されたか
# -1 は「まだ探索されていない」ことを表す
dist = [-1] * N

# todo リストを表すキュー
que = Queue()

# 頂点 0 を始点とする
dist[0] = 0
que.put(0)

ans=0
# キューが空になるまで探索する
while not que.empty():
    # キューから頂点を取り出す
    v = que.get()

    # 頂点 v から 1 手で行ける頂点 next_v を探索
    for next_v in G[v]:
        # 頂点 next_v が探索済みであれば何もしない
        if dist[next_v] != -1:
            continue
        if ans < next_v:
            ans=next_v
        # 頂点 next_v を探索する
        dist[next_v] = dist[v] + 1
        que.put(next_v)
ans = [k for k, v in dictAB.items() if v==ans]
print(ans[0])