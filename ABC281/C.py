import sys

N, T = map(int, input().split())
A = list(map(int, input().split()))

sum=sum(A)

loop=T//sum
T=T-sum*loop
# print(loop, sum)
# print(T)
for i in range(N):
    T-=A[i]
    if T<0:
        print(i+1, T+A[i])
        sys.exit()