N = int(input())
Q = int(input())

box=[[] for _ in range(N+1)]
num=[set() for _ in range(200001)]
for _ in range(Q):
    A = list(map(int, input().split()))
    if A[0]==1:
        box[A[2]].append(A[1])
        num[A[1]].add(A[2])
    elif A[0]==2:
        print(*sorted(box[A[1]]))
    else:
        print(*sorted(num[A[1]]))
