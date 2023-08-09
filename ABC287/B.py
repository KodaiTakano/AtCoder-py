N, M = map(int, input().split())
S = [input() for _ in range(N)]
T = [input() for _ in range(M)]

c=0
for s in S:
    for t in T:
        if s[3:]==t:
            c+=1
            break
print(c)