H, W = map(int, input().split())

A = [list(input()) for _ in range(H)]
B = [list(input()) for _ in range(H)]

# [print(*A[i]) for i in range(H)] 

for i in range(H):
    A[i].extend(A[i])
A.extend(A)
# [print(*A[i]) for i in range(2*H)]

from sys import exit
import numpy

A=numpy.array(A)
B=numpy.array(B)
for i in range(H):
    for j in range(W):
        # print(i, j)
        # print(A[i:i+H,j:j+W])
        if numpy.array_equal(A[i:i+H, j:j+W], B):
            print("Yes")
            exit()
print("No")