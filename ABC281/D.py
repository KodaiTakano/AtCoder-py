from collections import defaultdict

N, K, D = map(int, input().split())
A = sorted(list(map(int, input().split())))

d=defaultdict(int)
for a in A:
    d[a%D]+=1

for i in range(1, K):
    for k, v in d.items():
        d