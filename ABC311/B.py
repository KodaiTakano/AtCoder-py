N, D = map(int, input().split())
S = [list(input()) for _ in range(N)]

S = [list(x) for x in zip(*S)]
# print(S)
ans=0
c=0
for j in range(D):
    if "x" in S[j]:
        ans=max(c, ans)
        c=0
    else:
        c+=1
print(max(ans, c))