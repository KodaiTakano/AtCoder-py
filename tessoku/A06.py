N, Q = map(int, input().split())
A = list(map(int, input().split()))

s=[0]
crr=0
for a in A:
    crr+=a
    s.append(crr)

for _ in range(Q):
    L, R = map(int, input().split())
    print(s[R]-s[L-1])