N, K = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]

sum=0
for i in range(N):
    sum+=A[i][1]

from sys import exit
from bisect import bisect_right

A = sorted(A, reverse=True, key=lambda x: x[0]) #0列目を基準にして昇順ソート
# print(A)
for i in range(N-1):
    A[i+1][1]+=A[i][1]
# print(A)
B=[]
for i in range(N):
    B.append(A[i][1])
# print(B)
index=bisect_right(B, K)
if index==N:
    print(1)
else:
    print(A[index][0]+1)
