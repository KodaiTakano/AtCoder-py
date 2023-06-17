import heapq
from collections import defaultdict

N, K, Q = map(int, input().split())

A=[0]*N
# 使っている数字
used=[]
for i in range(N):
    if i<K:
        used.append(1)
    else:
        used.append(0)
# f内で使用の最小数字
min=0
ans=0
# 使っていない数字のリスト
unused=[]

for i in range(Q):
    X, Y = map(int, input().split())
    if used[X-1]==1:
        if Y>min:
            if A[X-1]==min:
                min=Y
            ans+=Y-A[X-1]
            A[X-1]=Y
        else:
            # ans+=(使っていない数字のリストの最大値)-Y
            # used[使っていない数字のリストの最大値のインデックス]=1
            A[X-1]=Y
            used[X-1]=0
            # min=(使っていない数字のリストの最大値)
    else:
        if Y>min:
            # unusedに使っている数字のリストの1番目の数を追加
            ans+=Y-min
            # if Y<(使っている数字のリストの2番目の数)
                # min=Y
            A[X-1]=Y
            used[X-1]=1
        else:
            # 使っていない数字のリストに追加