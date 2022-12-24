N = int(input())
H = list(map(int, input().split()))

A=[0]*N
A[1]=abs(H[0]-H[1])
for i in range(2, N):
    A[i]=min(A[i-1]+abs(H[i]-H[i-1]), A[i-2]+abs(H[i]-H[i-2]))
print(A[N-1])