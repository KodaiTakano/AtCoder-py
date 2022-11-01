N, Q = map(int, input().split())
A = list(map(int, input().split()))

# B[i]: A[i+1]-A[i]: 次の区画との差
B=[]
for i in range(N):
    B.append(abs(A[i+1]-A[i]))

