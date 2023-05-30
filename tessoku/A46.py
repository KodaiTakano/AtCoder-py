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
print(1)
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
    print(min_j+1)
    c+=1
print(1)