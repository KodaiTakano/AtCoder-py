import collections
import math

def combinations_count(n, k):
    return math.factorial(n) // (math.factorial(n - k) * math.factorial(k))
 
N = int(input())

d=collections.defaultdict(int)

for _ in range(N):
    A = int(input())
    d[A]+=1
    
ans=0
for v in d.values():
    if v==1:
        continue
    ans+=combinations_count(v,2)
print(ans)