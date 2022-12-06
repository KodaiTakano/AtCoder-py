from collections import defaultdict

N = int(input())
A = list(map(int, input().split()))
d=defaultdict(int)
for a in A:
    d[a]+=1
ans=0
for k1, v1 in d.items():
    for k2, v2 in d.items():
        if k1>=k2:
            continue
        ans+=(k2-k1)**2*v1*v2
print(ans)