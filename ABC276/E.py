from queue import Queue

# 入力
H, W = map(int, input().split())
B = [list(input().split()) for _ in range(H)]
for i in range(H):
    B[i] = list(B[i][0])
print(B)
    
S = [[2 for i in range(W+2)] for j in range(H+2)]
for i in range(H):
    for j in range(W):
        if B[i][j]=="S":
            S[i+1][j+1]==1
            start=[[i+1,j+1]]
        if B[i][j]=="#":
            S[i+1][j+1]=9
        if B[i][j]==".":
            S[i+1][j+1]=0
print(S)

pos = start
count =0
while len(pos) > 0:#探索可能ならTrue
    x, y = pos.pop(0) #リストから探索する位置を取得

    #ゴールについた時点で終了
    if S[x][y]==1 and count!=0:
        print("Yes")

    #探索済みとしてセット
    S[x][y] = 2

    #現在位置の上下左右を探索：〇<2は壁でもなく探索済みでもないものを示す
    if S[x-1][y] < 2:#左
        pos.append([x-1, y])
    if S[x+1][y] < 2:#右
        pos.append([x+1, y])
    if S[x][y-1] < 2:#上
        pos.append([x, y-1])
    if S[x][y+1] < 2:#下
        pos.append([x, y+1])
        
    count=1
print("No")