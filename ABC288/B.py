N, M = map(int, input().split())

ans=[]
for i in range(M):
    S = input()
    ans.append(S)

ans.sort()
print(*ans, sep="\n", end="")