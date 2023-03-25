R, C = map(int, input().split())
B = [list(input()) for _ in range(R)]
for i in range(R):
    for j in range(C):
        if B[i][j] not in ["#", "."]:
            for k in range(R):
                for l in range(C):
                    # print(B[i][j])
                    if abs(i-k)+abs(j-l)<=int(B[i][j]) and (B[k][l] in ["#", "."]):
                        B[k][l]="."

for i in range(R):
    for j in range(C):
        if B[i][j] not in ["#", "."]:
            B[i][j]="."

[print(*B[i], sep="") for i in range(R)]