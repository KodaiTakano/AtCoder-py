N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

import bisect

A=A+B
# print(*A)
A_set=sorted(set(A))
for i in range(N+M):
    index=bisect.bisect_left(A_set, A[i])
    A[i]=index+1
# print(*A)

print(*A[:N])
print(*A[N:])