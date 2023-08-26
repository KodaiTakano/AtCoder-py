N, H, X = map(int, input().split())
A = list(map(int, input().split()))
from sys import exit
for i in range(N):
    if H+A[i]>=X:
        print(i+1)
        exit()