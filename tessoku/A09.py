H, W, N = map(int, input().split())
B = [[0]*(W+1) for _ in range(H+1)]

for _ in range(N):
    a, b, c, d = map(int, input().split())
    B[a-1][b-1]+=1
    B[a-1][d]-=1
    B[c][d]+=1
    B[c][b-1]-=1

for i in range(1, H+1):
    for j in range(W+1):
        B[i][j]+=B[i-1][j]

for i in range(H+1):
    for j in range(1, W+1):
        B[i][j]+=B[i][j-1]

[print(*B[i][:W]) for i in range(H)]