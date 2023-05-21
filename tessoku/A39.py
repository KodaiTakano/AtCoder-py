N = int(input())
LR=[]
for _ in range(N):
    A = list(map(int, input().split()))
    LR.append(A)

LR = sorted(LR, reverse=False, key=lambda x: (x[1],x[0]))

ans=0
now=0
for i in range(N):
    if now<=LR[i][0]:
        ans+=1
        now=LR[i][1]
print(ans)