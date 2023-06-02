N = int(input())
X=[]
Y=[]
for i in range(N):
    x, y = map(int, input().split())
    X.append(x)
    Y.append(y)

# 巡回済み都市
done=[0]*N
c=0
i=0
done[i]=1
greedy_path=[0]
while(c!=N-1):
    min_dist=100000
    min_j=0
    for j in range(N):
        if done[j]==0:
            dist=((X[i]-X[j])**2+(Y[i]-Y[j])**2)**0.5
            if min_dist>dist:
                min_dist=dist
                min_j=j
    done[min_j]=1
    i=min_j
    greedy_path.append(min_j)
    c+=1
greedy_path.append(0)
greedy_sum=0
for i in range(N+1):
        greedy_sum+=((X[greedy_path[i]]-X[greedy_path[j]])**2+(Y[greedy_path[i]]-Y[greedy_path[j]])**2)**0.5

# 局所探索
# [1,...,1]をl~rの範囲で都市を反転させる
import random
local_path=greedy_path.copy()
min_sum=greedy_sum
c=0
while(c!=10000):
    c+=1
    l=random.randint(1, N-1)
    r=random.randint(1, N-1)
    if l>r:
        l, r = r, l
    
    # print(l, r)
    # print(local_path)
    for i in range(int((r+1-l)/2)):
        local_path[l+i], local_path[r-i] = local_path[r-i], local_path[l+i]
    # print(local_path)
    
    local_sum=0
    for i in range(N):
        local_sum+=((X[local_path[i]]-X[local_path[i+1]])**2+(Y[local_path[i]]-Y[local_path[i+1]])**2)**0.5
    
    if local_sum<min_sum:
        min_sum=local_sum
    else:
        for i in range(int((r+1-l)/2)):
            local_path[l+i], local_path[r-i] = local_path[r-i], local_path[l+i]
for i in range(N+1):
    print(local_path[i]+1)
    
    
