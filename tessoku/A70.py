from collections import deque

N, M = map(int, input().split())

A = list(map(int, input().split()))
B = [list(map(lambda x: int(x)-1, input().split())) for _ in range(M)]
# print(B)

# 入力
treeN = pow(2, N)
G = [[] for _ in range(treeN)]
for i in range(treeN):
    for j in range(M):
        n=pow(2, B[j][0])+pow(2, B[j][1])+pow(2, B[j][2])
        # print(n)
        next_v=i^n
        # 頂点 A から頂点 B への辺を張る
        G[i].append(next_v)

# [print(*G[i]) for i in range(treeN)] 
# from sys import exit
# exit()

# 各頂点が何手目に探索されたか
# -1 は「まだ探索されていない」ことを表す
dist = [-1] * treeN

# todo リストを表すキュー
que = deque()

s=0
for i in range(N):
    s+=A[i]*pow(2, i)

# 頂点 0 を始点とする
dist[s] = 0
que.append(s)

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

if dist[treeN-1]==-1:
    print(-1)
else:
    print(dist[treeN-1])