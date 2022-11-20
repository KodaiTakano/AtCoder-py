from collections import defaultdict

d = defaultdict(set)

N, Q = map(int, input().split())
follow={}
for i in range(Q):
    T, a, b = map(int, input().split())
    if T==1:
        d[a].add(b)
    if T==2:
        if b in d[a]:
            d[a].remove(b)
    if T==3:
        if b in d[a] and a in d[b]:
            print("Yes")
        else:
            print("No")
