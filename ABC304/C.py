N, D = map(int, input().split())

X=[]
Y=[]
for _ in range(N):
    x, y = map(int, input().split())
    X.append(x)
    Y.append(y)
    
from queue import Queue

have=[-1]*N
que=Queue()
have[0]=1
que.put(0)
while not que.empty():
    now=que.get()
    for i in range(N):
        if now==i or have[i]!=-1:
            continue
        
        # 圏内
        # print((X[now]-X[i])**2+(Y[now]-Y[i]))
        if (X[now]-X[i])**2+(Y[now]-Y[i])**2<=D**2:
            have[i]=1
            que.put(i)

for i in range(N):
    if have[i]==1:
        print("Yes")
    else:
        print("No")