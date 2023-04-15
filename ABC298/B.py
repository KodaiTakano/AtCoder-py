from sys import exit
from copy import deepcopy
N = int(input())

A = [list(map(int, input().split())) for _ in range(N)]
B = [list(map(int, input().split())) for _ in range(N)]


# 無回転
ok=1
for i in range(N):
    for j in range(N):
        if A[i][j]==1:
            if B[i][j]==0:
                ok=0
if ok==1:
    print("Yes")
    exit()

tempA=deepcopy(A)
ok=1
for i in range(N):
    for j in range(N):
        tempA[i][j]=A[N-j-1][i]
# [print(*tempA[i]) for i in range(N)]
for i in range(N):
    for j in range(N):
        if tempA[i][j]==1:
            if B[i][j]==0:
                ok=0
if ok==1:
    print("Yes")
    exit()

ok=1
for i in range(N):
    for j in range(N):
        tempA[i][j]=A[N-i-1][N-j-1]
# [print(*tempA[i]) for i in range(N)]
for i in range(N):
    for j in range(N):
        if tempA[i][j]==1:
            if B[i][j]==0:
                ok=0
if ok==1:
    print("Yes")
    exit()

ok=1
for i in range(N):
    for j in range(N):
        tempA[i][j]=A[j][N-i-1]
# [print(*tempA[i]) for i in range(N)]
for i in range(N):
    for j in range(N):
        if tempA[i][j]==1:
            if B[i][j]==0:
                ok=0
if ok==1:
    print("Yes")
    exit()

print("No")