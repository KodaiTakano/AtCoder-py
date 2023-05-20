H, W = map(int, input().split())
S = [list(input()) for _ in range(H)]

from sys import exit

for i in range(H):
    for j in range(W):
        if S[i][j]=="s":
            # 上方向
            if i>=4:
                if [S[i-1][j], S[i-2][j], S[i-3][j], S[i-4][j]]==["n", "u", "k", "e"]:
                    for k in range(5):
                        print(i-k+1, j+1)
                    exit()
            if i>=4 and j>=4:
                if [S[i-1][j-1], S[i-2][j-2], S[i-3][j-3], S[i-4][j-4]]==["n", "u", "k", "e"]:
                    for k in range(5):
                        print(i-k+1, j-k+1)
                    exit()
            if j>=4:
                if [S[i][j-1], S[i][j-2], S[i][j-3], S[i][j-4]]==["n", "u", "k", "e"]:
                    for k in range(5):
                        print(i+1, j-k+1)
                    exit()
            # 左下
            if i+4<=H-1 and j>=4:
                if [S[i+1][j-1], S[i+2][j-2], S[i+3][j-3], S[i+4][j-4]]==["n", "u", "k", "e"]:
                    for k in range(5):
                        print(i+k+1, j-k+1)
                    exit()
            if i+4<=H-1:
                if [S[i+1][j], S[i+2][j], S[i+3][j], S[i+4][j]]==["n", "u", "k", "e"]:
                    for k in range(5):
                        print(i+k+1, j+1)
                    exit()
            if i+4<=H-1 and j+4<=W-1:
                if [S[i+1][j+1], S[i+2][j+2], S[i+3][j+3], S[i+4][j+4]]==["n", "u", "k", "e"]:
                    for k in range(5):
                        print(i+k+1, j+k+1)
                    exit()
            if j+4<=W-1:
                if [S[i][j+1], S[i][j+2], S[i][j+3], S[i][j+4]]==["n", "u", "k", "e"]:
                    for k in range(5):
                        print(i+1, j+k+1)
                    exit()
            if i>=4 and j+4<=W-1:
                if [S[i-1][j+1], S[i-2][j+2], S[i-3][j+3], S[i-4][j+4]]==["n", "u", "k", "e"]:
                    for k in range(5):
                        print(i-k+1, j+k+1)
                    exit()