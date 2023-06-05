W, H = map(int, input().split())
N = int(input())
berry=[]
for _ in range(N):
    L = list(map(int, input().split()))
    berry.append(L)
A = int(input())
a = list(map(int, input().split()))
B = int(input())
b = list(map(int, input().split()))

from collections import defaultdict
import bisect

# d[1000000*A+B]: 上からA番目, 右からB番目のピースにあるいちごの数
d=defaultdict(int)

for i in range(N):
    d[1000000*bisect.bisect_left(a, berry[i][0])+bisect.bisect_right(b, berry[i][1])]+=1


if len(d)!=(A+1)*(B+1):
    print(0, max(d.values()))
else:
    print(min(d.values()), max(d.values()))