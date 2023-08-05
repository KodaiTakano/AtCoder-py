# 入力
N, M = map(int, input().split())
B = [list(map(int, input().split())) for _ in range(M)]
ans=[-1]*N

for i in range(M):
    ans[B[i][1]-1]=0
# print(ans)
for i in range(M):
    if ans[B[i][0]-1]==-1:
        ans[B[i][0]-1]=1
# print(ans)

from sys import exit

a=-1
for i in range(N):
    if ans[i]==1:
        if a!=-1:
            print(-1)
            exit()
        else:
            a=i+1
print(a)