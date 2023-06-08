import heapq

q=[]
heapq.heapify(q)

Q  = int(input())
for _ in range(Q):
    A = list(map(int, input().split()))
    if A[0]==1:
        heapq.heappush(q, A[1])
    elif A[0]==2:
        ANS=heapq.heappop(q)
        print(ANS)
        heapq.heappush(q, ANS)
    else:
        heapq.heappop(q)