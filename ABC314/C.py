from collections import deque

N, M = map(int, input().split())
S = list(input())
A = list(map(int, input().split()))

place=[deque() for _ in range(M)]
for i in range(N):
    place[A[i]-1].append(S[i])

# [print(*place[i]) for i in range(M)]

for i in range(M):
    l=place[i].pop()
    place[i].appendleft(l)

# [print(*place[i]) for i in range(M)]

for i in range(N):
    print(place[A[i]-1].popleft(), end="")