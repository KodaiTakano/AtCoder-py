from queue import Queue

# 入力
N, M = map(int, input().split())
G = [[] for i in range(N)]
for i in range(M):
    A, B = map(int, input().split())

    # 頂点 A から頂点 B への辺を張る
    G[A-1].append(B-1)
    G[B-1].append(A-1)

# todo リストを表すキュー
que = Queue()

que.put(0)

ans=[]
for v in range(N):
    ans.append(sorted(G[v]))
for i in range(N):
    print(len(ans[i]), *(map(lambda x: x+1, ans[i])))