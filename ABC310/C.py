N = int(input())
S = [input() for _ in range(N)]

from collections import defaultdict

d=defaultdict(int)

ans=0
for s in S:
    if s not in d.keys():
       ans+=1
    d[s]+=1
    d[s[::-1]]+=1
print(ans)