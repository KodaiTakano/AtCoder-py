H, W = map(int, input().split())
S = [list(input()) for _ in range(H)]
# print(S)

snuke="snuke"

# (i,j)は1000*i+j番目
G = [[] for _ in range(1000*H+W)]
for i in range(H):
    for j in range(W):
        if i==H-1 and j==W-1:
            break
        elif i==H-1:
            if S[i][j]=="s":
                if S[i][j+1]=="e":
                    G[1000*i+j+1].append(1000*i+j)
                if S[i][j+1]=="n":
                    G[1000*i+j].append(1000*i+j+1)
            if S[i][j]=="n":
                if S[i][j+1]=="s":
                    G[1000*i+j+1].append(1000*i+j)
                if S[i][j+1]=="u":
                    G[1000*i+j].append(1000*i+j+1)
            if S[i][j]=="u":
                if S[i][j+1]=="n":
                    G[1000*i+j+1].append(1000*i+j)
                if S[i][j+1]=="k":
                    G[1000*i+j].append(1000*i+j+1)
            if S[i][j]=="k":
                if S[i][j+1]=="u":
                    G[1000*i+j+1].append(1000*i+j)
                if S[i][j+1]=="e":
                    G[1000*i+j].append(1000*i+j+1)
            if S[i][j]=="e":
                if S[i][j+1]=="k":
                    G[1000*i+j+1].append(1000*i+j)
                if S[i][j+1]=="s":
                    G[1000*i+j].append(1000*i+j+1)
        elif j==W-1:
            if S[i][j]=="s":
                if S[i+1][j]=="e":
                    G[1000*(i+1)+j].append(1000*i+j)
                if S[i+1][j]=="n":
                    G[1000*i+j].append(1000*(i+1)+j)
            if S[i][j]=="n":
                if S[i+1][j]=="s":
                    G[1000*(i+1)+j].append(1000*i+j)
                if S[i+1][j]=="u":
                    G[1000*i+j].append(1000*(i+1)+j)
            if S[i][j]=="u":
                if S[i+1][j]=="n":
                    G[1000*(i+1)+j].append(1000*i+j)
                if S[i+1][j]=="k":
                    G[1000*i+j].append(1000*(i+1)+j)
            if S[i][j]=="k":
                if S[i+1][j]=="u":
                    G[1000*(i+1)+j].append(1000*i+j)
                if S[i+1][j]=="e":
                    G[1000*i+j].append(1000*(i+1)+j) 
            if S[i][j]=="e":
                if S[i+1][j]=="k": 
                    G[1000*(i+1)+j].append(1000*i+j)
                if S[i+1][j]=="s":
                    G[1000*i+j].append(1000*(i+1)+j)  
        else:
            if S[i][j]=="s":
                if S[i][j+1]=="e":
                    G[1000*i+j+1].append(1000*i+j)
                if S[i][j+1]=="n":
                    G[1000*i+j].append(1000*i+j+1)
            if S[i][j]=="n":
                if S[i][j+1]=="s":
                    G[1000*i+j+1].append(1000*i+j)
                if S[i][j+1]=="u":
                    G[1000*i+j].append(1000*i+j+1)
            if S[i][j]=="u":
                if S[i][j+1]=="n":
                    G[1000*i+j+1].append(1000*i+j)
                if S[i][j+1]=="k":
                    G[1000*i+j].append(1000*i+j+1)
            if S[i][j]=="k":
                if S[i][j+1]=="u":
                    G[1000*i+j+1].append(1000*i+j)
                if S[i][j+1]=="e":
                    G[1000*i+j].append(1000*i+j+1)
            if S[i][j]=="e":
                if S[i][j+1]=="k":
                    G[1000*i+j+1].append(1000*i+j)
                if S[i][j+1]=="s":
                    G[1000*i+j].append(1000*i+j+1)
            if S[i][j]=="s":
                if S[i+1][j]=="e":
                    G[1000*(i+1)+j].append(1000*i+j)
                if S[i+1][j]=="n":
                    G[1000*i+j].append(1000*(i+1)+j)
            if S[i][j]=="n":
                if S[i+1][j]=="s":
                    G[1000*(i+1)+j].append(1000*i+j)
                if S[i+1][j]=="u":
                    G[1000*i+j].append(1000*(i+1)+j)
            if S[i][j]=="u":
                if S[i+1][j]=="n":
                    G[1000*(i+1)+j].append(1000*i+j)
                if S[i+1][j]=="k":
                    G[1000*i+j].append(1000*(i+1)+j)
            if S[i][j]=="k":
                if S[i+1][j]=="u":
                    G[1000*(i+1)+j].append(1000*i+j)
                if S[i+1][j]=="e":
                    G[1000*i+j].append(1000*(i+1)+j) 
            if S[i][j]=="e":
                if S[i+1][j]=="k": 
                    G[1000*(i+1)+j].append(1000*i+j)
                if S[i+1][j]=="s":
                    G[1000*i+j].append(1000*(i+1)+j)

from queue import Queue

# 各頂点が何手目に探索されたか
# -1 は「まだ探索されていない」ことを表す
dist = [-1] * len(G)

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
        # 頂点 next_v が探索済みであれば何もしない
        if dist[next_v] != -1:
            continue

        # 頂点 next_v を探索する
        dist[next_v] = dist[v] + 1
        que.put(next_v)
# print(dist)
# for i in range(len(dist)):
#     if dist[i]!=-1:
#         print(int(i/1000), i%1000)
if dist[1000*(H-1)+W-1]!=-1:
    print("Yes")
else:
    print("No")