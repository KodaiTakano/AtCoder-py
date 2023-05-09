H, W = map(int, input().split())
B = [list(input()) for _ in range(H)]

for i in range(H):
    for j in range(W-1):
        if B[i][j]=="T" and B[i][j+1]=="T":
            B[i][j]="P"
            B[i][j+1]="C"

[print(*B[i], sep="") for i in range(H)]
