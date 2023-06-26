from sys import exit

HA, WA = map(int, input().split())
A = [list(input()) for _ in range(HA)]
HB, WB = map(int, input().split())
B = [list(input()) for _ in range(HB)]
HX, WX = map(int, input().split())
X = [list(input()) for _ in range(HX)]

Z=[["."]*30 for _ in range(30)]
# [print(*Z[i]) for i in range(30)]

# Z[10][10]とX[0][0]を重ねる
for i in range(HX):
    for j in range(WX):
        if X[i][j]=="#":
            Z[10+i][10+j]="#"
# [print(*Z[i]) for i in range(30)]

# 手順
# 全探索でXの中にAが全部入るか判定
# 入った時, Xの中にBが全部入るか判定
# 入った時, Xが全部埋まってるか判定

# Z中のXの#の場所
Xplace=set()
for i in range(30):
    for j in range(30):
        if Z[i][j]=="#":
            Xplace.add(100*i+j)
# print(Xplace)

# Aの左上の#の場所からどの位置に#があるか
Asharp=[[0,0]]
for i in range(HA):
    for j in range(WA):
        if A[i][j]=="#":
            Asharp.append([i-Asharp[0][0], j-Asharp[0][1]])
# print(Asharp)

# Xの中にAが全部入るパターンをXpalceと同じ形でlist in setで格納
Aplace_list=[]
for i in range(30-HA):
    for j in range(30-WA):
        XinA=True
        # ijを左上としたときのAの#の場所
        Aplace=set()
        # XinAであるかどうか
        # Aの#の場所にZの#があればいい
        for k in range(1, len(Asharp)):
            Aplace.add(100*(i+Asharp[k][0])+j+Asharp[k][1])
            if Z[i+Asharp[k][0]][j+Asharp[k][1]]!="#":
                XinA=False
        if XinA==True:
            Aplace_list.append(Aplace)
# print(Aplace_list)

# Bの左上のマスからどの位置に#があるか
Bsharp=[[0,0]]
for i in range(HB):
    for j in range(WB):
        if B[i][j]=="#":
            Bsharp.append([i-Bsharp[0][0], j-Bsharp[0][1]])

# Xの中にBが全部入るパターンをXpalceと同じ形でlist in setで格納
Bplace_list=[]
for i in range(30-HB):
    for j in range(30-WB):
        XinB=True
        # ijを左上としたときのAの#の場所
        Bplace=set()
        # XinBであるかどうか
        # Bの#の場所にZの#があればいい
        for k in range(1, len(Bsharp)):
            Bplace.add(100*(i+Bsharp[k][0])+j+Bsharp[k][1])
            if Z[i+Bsharp[k][0]][j+Bsharp[k][1]]!="#":
                XinB=False
        if XinB==True:
            Bplace_list.append(Bplace)

for a in Aplace_list:
    for b in Bplace_list:
        if a|b == Xplace:
            print("Yes")
            exit()
print("No")