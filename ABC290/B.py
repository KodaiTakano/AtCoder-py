N, K = map(int, input().split())
S = list(input())

for i in range(N):
    if K>0 and S[i]=='o':
        K-=1
    elif K==0 and S[i]=='o':
        S[i]='x'
print(*S, sep="")
        