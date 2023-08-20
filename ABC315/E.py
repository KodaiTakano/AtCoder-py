def topological_sort(G, into_num):
    #入ってくる有向辺を持たないノードを列挙
    q = deque()
    #V: 頂点数
    for i in range(N):
        if into_num[i]==0:
            q.append(i)
    
    #以下、幅優先探索
    ans = []
    while q:
        v = q.popleft()
        ans.append(v+1)
        for adj in G[v]:
            into_num[adj] -= 1 #入次数を減らす
            if into_num[adj]==0:
                q.append(adj) #入次数が0になったら、キューに入れる
    
    return ans

N = int(input())
A = [list(map(int, input().split())) for _ in range(N)]

from collections import deque

# 入力
G = [[] for _ in range(N)]
into_num = [0]*N
for i in range(N):
    for j in range(1, len(A[i])):
        G[i].append(A[i][j]-1)
        into_num[A[i][j]-1]+=1


# [print(*G[i]) for i in range(N)]
    
# 各頂点が何手目に探索されたか
# -1 は「まだ探索されていない」ことを表す
dist = [-1] * N

# todo リストを表すキュー
que = deque()

# 頂点 0 を始点とする
dist[0] = 0
que.append(0)
ans=[]

# キューが空になるまで探索する
while que:
    # キューから頂点を取り出す
    v = que.popleft()
    
    ans.append(v+1)

    # 頂点 v から 1 手で行ける頂点 next_v を探索
    for next_v in G[v]:
        # 頂点 next_v が探索済みであれば何もしない
        if dist[next_v] != -1:
            continue

        # 頂点 next_v を探索する
        dist[next_v] = dist[v] + 1
        que.append(next_v)

ans.reverse() 
ans=set(ans[:-1])
# print(*ans[:-1])


t=topological_sort(G, into_num)
t.reverse()

for i in range(N):
    if t[i] in ans:
        print(t[i], end=" ")