import heapq

N, D = map(int, input().split())
G=[[] for _ in range(D)]
for _ in range(N):
    A = list(map(int, input().split()))
    G[A[0]-1].append(A[1])
ans=0

q=[]
heapq.heapify(q)

ans=0
for d in range(D):
    for i in range(len(G[d])):
        heapq.heappush(q, -G[d][i])
    if q!=[]:
        ans-=heapq.heappop(q)
print(ans)
