import bisect


N = int(input())
A = sorted(list(map(int, input().split())))
# print(A)
Q = int(input())
for i in range(Q):
    B = int(input())
    idx = bisect.bisect_left(A, B)
    if idx==0:
        print(abs(B-A[0]))
    elif idx==N:
        print(abs(B-A[N-1]))
    else:
        print(min(abs(B-A[idx-1]), abs(B-A[idx])))