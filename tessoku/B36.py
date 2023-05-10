N, M = map(int, input().split())
S = list(input())

c=0
for s in S:
    if s=="1":
        c+=1

if c%2==M%2:
    print("Yes")
else:
    print("No")