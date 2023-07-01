from decimal import Decimal

N = int(input())
A=[]
for i in range(N):
    a, b = map(int, input().split())
    a=Decimal(a)
    b=Decimal(b)
    A.append([i, a/(a+b)])
# print(A)
A = sorted(A, reverse=True, key=lambda x: x[1])
# print(A)
for i in range(N):
    print(A[i][0]+1, end=" ")