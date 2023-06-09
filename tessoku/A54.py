from collections import defaultdict

d=defaultdict(int)

Q = int(input())
for _ in range(Q):
    S = list(input().split())
    if S[0]=="1":
        d[S[1]]=S[2]
    else:
        print(d[S[1]])