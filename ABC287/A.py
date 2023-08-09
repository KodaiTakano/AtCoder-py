N = int(input())
S = [input() for _ in range(N)]

a=0
f=0
for s in S:
    if s=="Against":
        a+=1
    else:
        f+=1
if a<f:
    print("Yes")
else:
    print("No")