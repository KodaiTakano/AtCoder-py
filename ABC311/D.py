from collections import deque

# 入力
N, M = map(int, input().split())
S = [list(input()) for _ in range(N)]

# 各頂点が何手目に探索されたか
# -1 は「まだ探索されていない」ことを表す
dist = [[-1]*M for _ in range(N)]
done=set()

# todo リストを表すキュー
que = deque()

# 頂点 0 を始点とする
dist[1][1] = 0
que.append([1,1])

# キューが空になるまで探索する
while que:
    # キューから頂点を取り出す
    # v[0]:上下, v[1]:左右
    v = que.popleft()
    
    # 上移動
    for i in range(v[0], -1, -1):
        # 岩に当たった時
        if S[i][v[1]]=="#":
            # 1個前が探索済みだった時
            if 1000*(i+1)+v[1] in done:
                break
            else:
                que.append([i+1, v[1]])
                done.add(1000*(i+1)+v[1])
                break
        else:
            dist[i][v[1]]=0
    # 下移動
    for i in range(v[0], N):
        # 岩に当たった時
        if S[i][v[1]]=="#":
            # 1個前が探索済みだった時
            if 1000*(i-1)+v[1] in done:
                break
            else:
                que.append([i-1, v[1]])
                done.add(1000*(i-1)+v[1])
                break
        else:
            dist[i][v[1]]=0
    # 右移動
    for i in range(v[1], M):
        # 岩に当たった時
        if S[v[0]][i]=="#":
            # 1個前が探索済みだった時
            if 1000*v[0]+i-1 in done:
                break
            else:
                que.append([v[0], i-1])
                done.add(1000*v[0]+i-1)
                break
        else:
            dist[v[0]][i]=0
    # 右移動
    for i in range(v[1], -1, -1):
        # 岩に当たった時
        if S[v[0]][i]=="#":
            # 1個前が探索済みだった時
            if 1000*v[0]+i+1 in done:
                break
            else:
                que.append([v[0], i+1])
                done.add(1000*v[0]+i+1)
                break
        else:
            dist[v[0]][i]=0
# [print(*dist[i]) for i in range(N)]
ans=0
for i in range(N):
    for j in range(M):
        if dist[i][j]==0:
            ans+=1
print(ans)