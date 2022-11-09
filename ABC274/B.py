H, W = map(int, input().split())

C = [list(input()) for _ in range(H)]
for i in range(W):
    ans = 0
    for j in range(H):
        if C[j][i]=='#':
            ans+=1
    print(ans, end=" ")