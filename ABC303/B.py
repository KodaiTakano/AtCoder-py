N, M = map(int, input().split())

A = [list(map(int, input().split())) for _ in range(M)]

ansl=[[0]*N for _ in range(N)]
for i in range(M):
    for j in range(N-1):
        ansl[A[i][j]-1][A[i][j+1]-1]=1
        ansl[A[i][j+1]-1][A[i][j]-1]=1
        
ans=0
for i in range(N):
    for j in range(i+1, N):
        if ansl[i][j]==0:
            ans+=1

print(ans)