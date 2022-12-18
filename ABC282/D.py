from collections import deque
from sys import exit


# 入力
N, M = map(int, input().split())

count=[0 for _ in range(N)]

G = [[] for i in range(N)]
for i in range(M):
    A, B = map(int, input().split())

    # 頂点 A から頂点 B への辺を張る
    G[A-1].append(B-1)
    G[B-1].append(A-1)

    if A-1<B-1:
        count[A-1]+=1
    else:
        count[B-1]+=1

color = [-1 for _ in range(N)]    # color[v]：頂点 v の色が黒なら 1, 白なら 0, 未探索なら -1
ok = 'Yes'
# 全ての頂点について
for v in range(N):
    if color[v] != -1: continue
    # 頂点 v の色を白で決め打ちしたうえで、幅優先探索を行う
    deq = deque([]) # 探索候補の頂点番号を入れるキュー
    color[v] = 0
    deq.append(v)
    # キューに要素が残っている限り
    while len(deq) > 0:
        qv = deq.popleft()
        # 頂点 qv に隣接している頂点 nv について、
        for nv in G[qv]:
            # nv がすでに探索済みならば、スキップする
            if color[nv] != -1:
                # 隣り合う頂点どうしが同じ色なら、答えは No
                if color[nv] == color[qv]: ok = 'No'
                continue

            # そうでなければ、頂点 nv の色を color[qv] と逆にしたうえで、nv も探索候補に入れる
            color[nv] = 1 - color[qv]
            deq.append(nv)
if ok=="No":
    print(0)
    exit()

different_color_count=[0 for _ in range(N)]
siro_count=0
kuro_count=0
for i in range(N):
    if color[N-1-i]==0:
        siro_count+=1
    else:
        kuro_count+=1
    if color[N-1-i]==0:
        different_color_count[N-i-1]=kuro_count
    else:
        different_color_count[N-i-1]=siro_count
# print(different_color_count)
# print(count)
ans=0
for i in range(N):
    ans+=different_color_count[i]-count[i]
print(ans)