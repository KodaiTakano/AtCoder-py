from queue import Queue
from bisect import bisect_left, bisect_right, bisect
import sys

# 入力
N = int(input())
A=[]
B=[]
AB=[]
for _ in range(N):
    a = list(map(int, input().split()))
    A.append(a[0])
    B.append(a[1])
    AB.append(a)
A=sorted(A)
B=sorted(B)
AB=sorted(AB)
print(AB)

set_AB=list(set(A+B))
if set_AB[0]!=1:
    print(0)
    sys.exit()
idx=0
dic_ab={}
for i in set_AB:
    dic_ab[i]=idx
    idx+=1
for i in range(N):
    AB[i][0]=dic_ab[AB[i][0]]
    AB[i][1]=dic_ab[AB[i][1]]
print(AB)

n = len(dic_ab)
G=[[] for _ in range(n)]
for i in range(2*n):
    # 頂点 A から頂点 B への辺を張る
    G[AB[i][0]].append(AB[i][1])
    G[AB[i][1]].append(AB[i][0])


# todo リストを表すキュー
que = Queue()

# 頂点 1 を始点とする
dist=[-1]*n
dist[0]=0
que.put(0)

ans = 1
while not que.empty():
    # キューから頂点を取り出す
    v = que.get()

    # 頂点 v から 1 手で行ける頂点 next_v を探索
    for next_v in G[v]:
        # 頂点 next_v が探索済みであれば何もしない
        if dist[next_v] != -1:
            continue
        if ans < next_v:
            ans = next_v
        # 頂点 next_v を探索する
        dist[next_v] = dist[v] + 1
        que.put(next_v)
print(ans)
        