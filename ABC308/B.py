N, M = map(int, input().split())
C = list(input().split())
D = list(input().split())
P  = list(map(int, input().split()))

ans=0
for i in range(N):
    c=C[i]
    for j in range(M):
        if D[j]==c:
            ans+=P[j+1]
            break
        if j==M-1:
            ans+=P[0]
print(ans)