N, M = map(int, input().split())
S=[]
for _ in range(N):
    A = list(input())
    S.append(A)

ans=0
for i in range(N):
    for j in range(i+1, N):
        for k in range(M):
            if S[i][k]!="o" and S[j][k]!="o":
                break
            if k==M-1:
                ans+=1
print(ans)