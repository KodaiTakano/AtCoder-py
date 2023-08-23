N = int(input())
A = [list(map(int, input().split())) for _ in range(N)]

X=[0]*N
Y=[0]*N
for i in range(N):
    for j in range(N):
        if A[i][j]!=0:
            X[A[i][j]-1]=j
            Y[A[i][j]-1]=i

ans=0
for i in range(N):
    for j in range(i, N):
        if X[i]>X[j]:
            ans+=1

for i in range(N):
    for j in range(i, N):
        if Y[i]>Y[j]:
            ans+=1

print(ans)