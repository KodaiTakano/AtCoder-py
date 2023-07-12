H, W  = map(int, input().split())
sx, sy = map(int, input().split())
gx, gy = map(int, input().split())
S = [list(input()) for _ in range(H)]

from collections import deque

# 各頂点が何手目に探索されたか
# -1 は「まだ探索されていない」ことを表す
dist = [[-1]*W for _ in range(H)]

# todo リストを表すキュー
que = deque()

# 頂点 0 を始点とする
dist[sx-1][sy-1] = 0
que.append([sx-1, sy-1])

move=[[-1,0], [0,-1], [1,0], [0,1]]
# キューが空になるまで探索する
while que:
    # キューから頂点を取り出す
    v = que.popleft()

    # 頂点 v から 1 手で行ける頂点 next_v を探索
    for m in move:
        x=v[0]+m[0]
        y=v[1]+m[1]
        if 0<=x<H and 0<=y<W:
            if S[x][y]==".":
                # 頂点 next_v が探索済みであれば何もしない
                if dist[x][y] != -1:
                    continue

                # 頂点 next_v を探索する
                dist[x][y] = dist[v[0]][v[1]] + 1
                que.append([x,y])

# [print(*dist[i]) for i in range(H)]
print(dist[gx-1][gy-1])