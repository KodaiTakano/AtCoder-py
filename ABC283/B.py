N = int(input())
A = list(map(int, input().split()))
Q = int(input())

for i in range(Q):
    B = list(map(int, input().split()))
    if B[0]==1:
        A[B[1]-1]=B[2]
    else:
        print(A[B[1]-1])