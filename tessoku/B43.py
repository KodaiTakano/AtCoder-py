N, M = map(int, input().split())
A = list(map(int, input().split()))

ans=[M]*N
for a in A:
    ans[a-1]-=1

for a in ans:
    print(a)