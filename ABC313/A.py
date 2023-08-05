N = int(input())

A = list(map(int, input().split()))

from sys import exit

if max(A)==A[0]:
    for i in range(1, N):
        if A[i]==max(A):
            print(1)
            exit()
    print(0)
else:
    print(max(A)-A[0]+1)