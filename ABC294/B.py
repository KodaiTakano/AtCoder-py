H, W = map(int, input().split())
B = [list(map(int, input().split())) for _ in range(H)]

ABC = "abcdefghijklmnopqrstuvwxyz"
ABC=ABC.upper()

for i in range(H):
    for j in range(W):
        if B[i][j]==0:
            B[i][j]="."
        else:
            B[i][j]=ABC[B[i][j]-1]
[print(*B[i], sep="") for i in range(H)]