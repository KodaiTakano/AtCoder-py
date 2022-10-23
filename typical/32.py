import itertools


N = int(input())
A = [list(map(int, input().split())) for _ in range(N)]
M = int(input())
Z=[]
for i in range(M):
    x, y = map(int, input().split())
    Z.append([x,y])
    Z.append([y,x])
    

l=[]
for i in range(N):
    l.append(i+1)
    
ans = 1000000
for v in itertools.permutations(l):
    flag = False
    sum=0
    for i in range(N):
        sum += A[i][v[i]-1]
        if i < N-1:
            if [v[i],v[i+1]] in Z:
                flag=True
    if flag==False:
        ans = min(ans, sum)
if ans==1000000:
    print(-1)
else:
    print(ans)