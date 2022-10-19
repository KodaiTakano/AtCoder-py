N, K = map(int, input().split())

A=[]
for i in range(N):
    a = list(map(int, input().split()))
    A.append(a)
A = sorted(A, reverse=False, key=lambda x: x[0])  #1行目に注目してソート
print(A)