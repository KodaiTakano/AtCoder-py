N, M = map(int, input().split())
G = [[] for _ in range(N)]
for i in range(M):
    A, B = map(int, input().split())

    # 頂点 A から頂点 B への辺を張る
    G[A-1].append(B-1)
    G[B-1].append(A-1)

for i in range(N):
    print(i+1, ": {", sep="", end="")
    for j in range(len(G[i])):
        print(G[i][j]+1, end="")
        if j!=len(G[i])-1:
            print(",", end=" ")
    print("}")
