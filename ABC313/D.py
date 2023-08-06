N, K = map(int, input().split())

res=[]
for i in range(K+1):
    q=[]
    for j in range(K):
        if i+j>=K+1:
            j-=K+1
        q.append(i+j+1)
    
    print("?", *q)
    # n = int(input())
    # res.append(n)

ans=[-1]*N
res=[0,0,1,0]

for i in range(K+1):
    index=i+K
    # print(index)
    if index>K:
        index-=K+1
    if (sum(res)-res[i])%2==0:
        ans[index]=0
    else:
        ans[index]=1
# print(*ans)
# from sys import exit
# exit()
r=-1
if sum(ans[:K-1])%2==0:
    r=0
else:
    r=1

q=[]
for j in range(K-1):
    q.append(j+1)

for i in range(N-K-1):
    index=i+K+1
    q.append(index+1)
    print("?", *q)
    n = int(input())
    if (r+n)%2==0:
        ans[index]=0
    else:
        ans[index]=1
    q=q[:-1]
print("!", *ans)