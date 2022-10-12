import sys


H, W = map(int, input().split())

A = [list(map(int, input().split())) for _ in range(H)]
B = [list(map(int, input().split())) for _ in range(H)]

count = 0
for i in range(H-1):
    for j in range(W-1):
        x=A[i][j]-B[i][j]
        count+=abs(x)
        A[i][j]-=x
        A[i][j+1]-=x
        A[i+1][j]-=x
        A[i+1][j+1]-=x
[print(*A[i]) for i in range(H)]
for i in range(H):
    if A[i][W-1]!=B[i][W-1]:
        print("No")
        sys.exit()
for i in range(W):
    if A[H-1][i]!=B[H-1][i]:
        print("No")
        sys.exit()
print("Yes")
print(count)