N, L = map(int, input().split())
B = [list(input().split()) for _ in range(N)]

ans=0
for i in range(N):
    if B[i][1]=="E":
        ans=max(ans, L-int(B[i][0]))
    else:
        ans=max(ans, int(B[i][0]))
print(ans)