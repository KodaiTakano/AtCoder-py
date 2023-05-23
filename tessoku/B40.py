N = int(input())
A = list(map(int, input().split()))

c=[0]*100

for i in range(N):
    c[A[i]%100]+=1

ans=0
for i in range(1, 50):
    ans+=c[i]*c[100-i]

# 0と50の時
# x1/(2!*x2)=x!/(2!*(x-2)!)
if c[0]!=1:
    x1=1
    x2=1
    for i in range(2, c[0]+1):
        if i==c[0]-1:
            x2=x1
        x1*=i
    ans+=x1/(2*x2)

if c[50]!=1:
    x1=1
    x2=1
    for i in range(2, c[50]+1):
        if i==c[50]-1:
            x2=x1
        x1*=i
    ans+=x1/(2*x2)

print(int(ans))