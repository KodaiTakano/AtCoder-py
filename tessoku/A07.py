D = int(input())
N = int(input())

B=[0]*(D+1)
for _ in range(N):
    L, R = map(int, input().split())
    B[L-1]+=1
    B[R]-=1
# print(B)
ans=0
for i in range(D):
    ans+=B[i]
    print(ans)