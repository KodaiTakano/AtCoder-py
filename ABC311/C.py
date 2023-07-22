from collections import deque

# 入力
N = int(input())
G = [[] for _ in range(N)]
A = list(map(int, input().split()))
for i in range(N):
    # 頂点 A から頂点 B への辺を張る
    G[i].append(A[i]-1)

# 各頂点が何手目に探索されたか
# -1 は「まだ探索されていない」ことを表す
dist = [-1] * N

# todo リストを表すキュー
que = deque()

# 頂点 0 を始点とする
dist[0] = 0
que.append(0)

b=0
# キューが空になるまで探索する
while que:
    # キューから頂点を取り出す
    v = que.popleft()

    # 頂点 v から 1 手で行ける頂点 next_v を探索
    for next_v in G[v]:
        # 頂点 next_v が探索済みであれば何もしない
        if dist[next_v] != -1:
            b=next_v
            break

        # 頂点 next_v を探索する
        dist[next_v] = dist[v] + 1
        que.append(next_v)
    
    if b!=0:
        break

from sys import exit

ans=[b+1]
while 1:
    for i in range(len(G[b])):
        next_v = G[b][i]
        if dist[next_v]==dist[b]+1:
            ans.append(next_v+1)
            b=next_v
            continue
        if i ==len(G[b])-1:
            print(len(ans))
            print(*ans)
            exit()
            
    